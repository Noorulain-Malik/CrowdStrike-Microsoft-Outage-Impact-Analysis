import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sentiment scores
sentiment_df = pd.read_csv('C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\Airline_Analysis\\Airline_sentiment_scores.csv')

# Plot Sentiment Trends (Line Chart) without Compound Score
plt.figure(figsize=(12, 8))
plt.plot(sentiment_df['Time Period'], sentiment_df['pos'], marker='o', label='Positive', linestyle='-', color='#1f77b4')  # Dark Blue
plt.plot(sentiment_df['Time Period'], sentiment_df['neu'], marker='o', label='Neutral', linestyle='-', color='#4c8cbb')  # Medium Blue
plt.plot(sentiment_df['Time Period'], sentiment_df['neg'], marker='o', label='Negative', linestyle='-', color='#7ba7cf')  # Light Blue
plt.xlabel('Time Period')
plt.ylabel('Average Sentiment Score')
plt.title('Sentiment Trends Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart for Average Sentiment Scores without Compound Score
plt.figure(figsize=(12, 8))
bar_width = 0.3
x = range(len(sentiment_df['Time Period']))

plt.bar([p - bar_width for p in x], sentiment_df['pos'], width=bar_width, label='Positive', color='#1f77b4')  # Dark Blue
plt.bar(x, sentiment_df['neu'], width=bar_width, label='Neutral', color='#4c8cbb')  # Medium Blue
plt.bar([p + bar_width for p in x], sentiment_df['neg'], width=bar_width, label='Negative', color='#7ba7cf')  # Light Blue

plt.xticks(x, sentiment_df['Time Period'])
plt.xlabel('Time Period')
plt.ylabel('Average Sentiment Score')
plt.title('Average Sentiment Scores by Time Period')
plt.legend()
plt.show()

# Stacked Area Chart without Compound Score
plt.figure(figsize=(12, 8))
plt.fill_between(sentiment_df['Time Period'], sentiment_df['pos'], color="#1f77b4", alpha=0.5, label='Positive')  # Dark Blue
plt.fill_between(sentiment_df['Time Period'], sentiment_df['pos'] + sentiment_df['neu'], sentiment_df['pos'], color="#4c8cbb", alpha=0.5, label='Neutral')  # Medium Blue
plt.fill_between(sentiment_df['Time Period'], sentiment_df['pos'] + sentiment_df['neu'] + sentiment_df['neg'], sentiment_df['pos'] + sentiment_df['neu'], color="#7ba7cf", alpha=0.5, label='Negative')  # Light Blue

plt.xlabel('Time Period')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Distribution Over Time')
plt.legend()
plt.show()

# Heatmap without Compound Score
plt.figure(figsize=(12, 8))
sns.heatmap(sentiment_df.set_index('Time Period').drop(columns=['compound']), annot=True, cmap='Blues', fmt=".2f")
plt.title('Sentiment Heatmap Over Time')
plt.show()

# Box Plot (Remove Compound and use Blue Shades)
plt.figure(figsize=(12, 8))
# Assuming `df` is your DataFrame for the box plot
df['period'] = pd.cut(pd.to_datetime(df['created']), bins=pd.to_datetime(list(time_periods.values())), labels=list(time_periods.keys()))
sns.boxplot(data=df, x='period', y='neg', palette='Blues')
plt.title('Distribution of Negative Sentiment Scores by Time Period')
plt.show()

sns.boxplot(data=df, x='period', y='neu', palette='Blues')
plt.title('Distribution of Neutral Sentiment Scores by Time Period')
plt.show()

sns.boxplot(data=df, x='period', y='pos', palette='Blues')
plt.title('Distribution of Positive Sentiment Scores by Time Period')
plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the sentiment scores
# sentiment_df = pd.read_csv('C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\Airline_Analysis\\Airline_sentiment_scores.csv')

# # Bar Chart for Average Sentiment Scores without Compound Score
# plt.figure(figsize=(12, 8))
# bar_width = 0.3
# x = range(len(sentiment_df['Time Period']))

# # Plot the bars with updated colors
# plt.bar([p - bar_width for p in x], sentiment_df['pos'], width=bar_width, label='Positive', color='#2ca02c')  # Green
# plt.bar(x, sentiment_df['neu'], width=bar_width, label='Neutral', color='#1f77b4')  # Blue
# plt.bar([p + bar_width for p in x], sentiment_df['neg'], width=bar_width, label='Negative', color='#d62728')  # Red

# plt.xticks(x, sentiment_df['Time Period'])
# plt.xlabel('Time Period')
# plt.ylabel('Average Sentiment Score')
# plt.title('Average Sentiment Scores by Time Period')
# plt.legend()
# plt.show()
