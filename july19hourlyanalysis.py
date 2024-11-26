import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load your data
df = pd.read_csv('C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\Airline_Analysis\\Airline_filtered_combined_data.csv')

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define sentiment analysis function
def analyze_sentiment(text):
    if isinstance(text, str):  # Ensure the text is a string
        return analyzer.polarity_scores(text)
    return {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}

# Ensure 'content' column exists
if 'content' not in df.columns:
    raise KeyError("The 'content' column is missing from the DataFrame. Ensure that the data contains a 'content' column.")

# Handle missing values in 'content' column
df['content'] = df['content'].fillna('')

# Apply sentiment analysis and create sentiment columns
df[['compound', 'neg', 'neu', 'pos']] = df['content'].apply(lambda x: pd.Series(analyze_sentiment(x)))

# Convert 'created' column to datetime
df['created'] = pd.to_datetime(df['created'])

# Filter data for July 19, 2024
start_time = '2024-07-19 00:00:00'
end_time = '2024-07-19 23:59:59'
july_19_df = df[(df['created'] >= start_time) & (df['created'] <= end_time)]

# Extract hour from the 'created' column
july_19_df['hour'] = july_19_df['created'].dt.hour

# Calculate average sentiment scores by hour
hourly_sentiment = july_19_df.groupby('hour')[['compound', 'neg', 'neu', 'pos']].mean().reset_index()

# plt.figure(figsize=(12, 8))
# plt.plot(hourly_sentiment['hour'], hourly_sentiment['compound'], marker='o', label='Compound', color='cyan')
# plt.plot(hourly_sentiment['hour'], hourly_sentiment['pos'], marker='o', label='Positive', color='green')
# plt.plot(hourly_sentiment['hour'], hourly_sentiment['neu'], marker='o', label='Neutral', color='blue')
# plt.plot(hourly_sentiment['hour'], hourly_sentiment['neg'], marker='o', label='Negative', color='red')

# plt.fill_between(hourly_sentiment['hour'], hourly_sentiment[['compound', 'pos', 'neu', 'neg']].min(axis=1), hourly_sentiment[['compound', 'pos', 'neu', 'neg']].max(axis=1), color='grey', alpha=0.1)

# plt.xlabel('Hour of the Day')
# plt.ylabel('Average Sentiment Score')
# plt.title('Hourly Sentiment Scores on July 19, 2024')
# plt.legend()
# plt.grid(True)
# plt.xticks(range(24))
# plt.show()

plt.figure(figsize=(12, 8))
plt.fill_between(hourly_sentiment['hour'], hourly_sentiment['compound'], color="cyan", alpha=0.5, label='Compound')
plt.fill_between(hourly_sentiment['hour'], hourly_sentiment['compound'] + hourly_sentiment['pos'], hourly_sentiment['compound'], color="green", alpha=0.5, label='Positive')
plt.fill_between(hourly_sentiment['hour'], hourly_sentiment['compound'] + hourly_sentiment['pos'] + hourly_sentiment['neu'], hourly_sentiment['compound'] + hourly_sentiment['pos'], color="blue", alpha=0.5, label='Neutral')
plt.fill_between(hourly_sentiment['hour'], hourly_sentiment['compound'] + hourly_sentiment['pos'] + hourly_sentiment['neu'] + hourly_sentiment['neg'], hourly_sentiment['compound'] + hourly_sentiment['pos'] + hourly_sentiment['neu'], color="red", alpha=0.5, label='Negative')

plt.xlabel('Hour of the Day')
plt.ylabel('Average Sentiment Score')
plt.title('Hourly Sentiment Scores on July 19, 2024')
plt.legend()
plt.grid(True)
plt.show()
