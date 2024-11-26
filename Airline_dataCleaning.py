import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the data
posts_df = pd.read_csv('C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\OverallReddit_analysis\\reddit_posts_final.csv')
comments_df = pd.read_csv('c:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\OverallReddit_analysis\\reddit_comments_final.csv')

# Define airline-related keywords
airline_keywords = ['airline', 'flight', 'plane', 'airport', 'airlines', 'aviation', 'Microsoft outage']

# Filter posts containing airline-related keywords in the title or body
filtered_posts_df = posts_df[
    posts_df['title'].str.contains('|'.join(airline_keywords), case=False, na=False) |
    posts_df['body'].str.contains('|'.join(airline_keywords), case=False, na=False)
]

# Filter comments containing airline-related keywords in the body
filtered_comments_df = comments_df[
    comments_df['body'].str.contains('|'.join(airline_keywords), case=False, na=False)
]

# Make copies of the filtered DataFrames to avoid SettingWithCopyWarning
filtered_posts_df = filtered_posts_df.copy()
filtered_comments_df = filtered_comments_df.copy()

# Update the 'type' column in the copied DataFrames
filtered_posts_df['type'] = 'post'
filtered_comments_df['type'] = 'comment'

# Rename columns to have a common format
filtered_posts_df.rename(columns={'id': 'identifier', 'title': 'title_or_comment', 'body': 'content'}, inplace=True)
filtered_comments_df.rename(columns={'comment_id': 'identifier', 'body': 'content'}, inplace=True)

# Combine the filtered DataFrames
combined_df = pd.concat([filtered_posts_df, filtered_comments_df], ignore_index=True)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define sentiment analysis function
def analyze_sentiment(text):
    if isinstance(text, str):  # Ensure the text is a string
        return analyzer.polarity_scores(text)
    return {'neg': 0, 'neu': 0, 'pos': 0}

# Apply sentiment analysis and create sentiment columns
combined_df[['neg', 'neu', 'pos']] = combined_df['content'].apply(lambda x: pd.Series({key: analyze_sentiment(x)[key] for key in ['neg', 'neu', 'pos']}))

# Convert 'created' to datetime format
combined_df['created'] = pd.to_datetime(combined_df['created'])

# Define time periods for filtering
time_periods = {
    'During': ('2024-07-19', '2024-07-25'),
    'After': ('2024-07-26', '2024-08-10')
}

# Function to calculate average sentiment scores
def calculate_sentiment_scores(df, period_start, period_end):
    period_df = df[(df['created'] >= period_start) & (df['created'] <= period_end)]
    sentiment_scores = period_df[['neg', 'neu', 'pos']].mean()
    return sentiment_scores

# Calculate sentiment scores for each time period
sentiment_scores = {}
for period, (start, end) in time_periods.items():
    sentiment_scores[period] = calculate_sentiment_scores(combined_df, start, end)

# Convert to DataFrame for plotting
sentiment_df = pd.DataFrame(sentiment_scores).T
sentiment_df.reset_index(inplace=True)
sentiment_df.rename(columns={'index': 'Time Period'}, inplace=True)

# Plotting the sentiment scores
plt.figure(figsize=(10, 6))
sns.barplot(x='Time Period', y='value', hue='variable', data=pd.melt(sentiment_df, id_vars='Time Period'))
plt.title('Average Sentiment Scores During and After the Incident')
plt.xlabel('Time Period')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Sentiment', loc='upper right', labels=['Negative', 'Neutral', 'Positive'])
plt.show()

# Save the filtered and analyzed data to a CSV file
combined_df.to_csv('Airline_filtered_combined_data.csv', index=False)

print("Filtered and analyzed data saved to 'Airline_filtered_combined_data.csv'.")
