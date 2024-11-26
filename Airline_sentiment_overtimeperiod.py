import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load your data
df = pd.read_csv('C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\Airline_Analysis\\Airline_filtered_combined_data.csv')

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define sentiment analysis function
def analyze_sentiment(text):
    if isinstance(text, str):  # Ensure the text is a string
        return analyzer.polarity_scores(text)
    return { 'neg': 0, 'neu': 0, 'pos': 0}



# Apply sentiment analysis and create sentiment columns
df[['neg', 'neu', 'pos']] = df['content'].apply(lambda x: pd.Series({key: analyze_sentiment(x)[key] for key in ['neg', 'neu', 'pos']}))


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
    sentiment_scores[period] = calculate_sentiment_scores(df, start, end)

# Convert to DataFrame for plotting
sentiment_df = pd.DataFrame(sentiment_scores).T
sentiment_df.reset_index(inplace=True)
sentiment_df.rename(columns={'index': 'Time Period'}, inplace=True)
print(sentiment_df) 


