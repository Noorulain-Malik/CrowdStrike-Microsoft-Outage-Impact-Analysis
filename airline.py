import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
posts_df = pd.read_csv('posts_with_sentiment.csv')
comments_df = pd.read_csv('comments_with_sentiment.csv')

# Set up the visualization style
sns.set(style="whitegrid")

# Visualization 1: Distribution of Sentiment Scores for Posts
plt.figure(figsize=(14, 7))

plt.subplot(2, 2, 1)
sns.histplot(posts_df['positive_score'], bins=30, kde=True, color='green')
plt.title('Distribution of Positive Scores (Posts)')
plt.xlabel('Positive Score')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
sns.histplot(posts_df['negative_score'], bins=30, kde=True, color='red')
plt.title('Distribution of Negative Scores (Posts)')
plt.xlabel('Negative Score')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
sns.histplot(posts_df['neutral_score'], bins=30, kde=True, color='blue')
plt.title('Distribution of Neutral Scores (Posts)')
plt.xlabel('Neutral Score')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)
sns.histplot(posts_df['compound_score'], bins=30, kde=True, color='purple')
plt.title('Distribution of Compound Scores (Posts)')
plt.xlabel('Compound Score')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Visualization 2: Sentiment Scores Over Time for Posts
plt.figure(figsize=(14, 7))

# Convert 'created' to datetime for better plotting
posts_df['created'] = pd.to_datetime(posts_df['created'])

# Plot sentiment scores over time
plt.subplot(2, 2, 1)
sns.lineplot(data=posts_df, x='created', y='positive_score', color='green')
plt.title('Positive Score Over Time (Posts)')
plt.xlabel('Date')
plt.ylabel('Positive Score')

plt.subplot(2, 2, 2)
sns.lineplot(data=posts_df, x='created', y='negative_score', color='red')
plt.title('Negative Score Over Time (Posts)')
plt.xlabel('Date')
plt.ylabel('Negative Score')

plt.subplot(2, 2, 3)
sns.lineplot(data=posts_df, x='created', y='neutral_score', color='blue')
plt.title('Neutral Score Over Time (Posts)')
plt.xlabel('Date')
plt.ylabel('Neutral Score')

plt.subplot(2, 2, 4)
sns.lineplot(data=posts_df, x='created', y='compound_score', color='purple')
plt.title('Compound Score Over Time (Posts)')
plt.xlabel('Date')
plt.ylabel('Compound Score')

plt.tight_layout()
plt.show()

# Visualization 3: Sentiment Scores by Time Range for Comments
plt.figure(figsize=(14, 7))

sns.boxplot(data=comments_df, x='time_range', y='compound_score', palette='Set2')
plt.title('Compound Sentiment Score by Time Range (Comments)')
plt.xlabel('Time Range')
plt.ylabel('Compound Score')

plt.xticks(rotation=45)
plt.show()
