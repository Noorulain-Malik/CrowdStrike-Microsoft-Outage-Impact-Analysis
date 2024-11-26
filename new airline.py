import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Manually create the sentiment scores
data = {
    'Time Period': ['During', 'After'],
    'Positive': [0.1, 0.2],  # Positive sentiment is low but slightly increases after
    'Negative': [0.7, 0.5],  # High negative sentiment during, slightly lower after
    'Neutral': [0.2, 0.3]    # Neutral sentiment balances out after the incident
}

# Convert to DataFrame
sentiment_df = pd.DataFrame(data)

# Melt the DataFrame for Seaborn plotting
melted_df = sentiment_df.melt(id_vars='Time Period', var_name='Sentiment', value_name='Score')

# Plotting the sentiment scores
plt.figure(figsize=(10, 6))
sns.barplot(x='Time Period', y='Score', hue='Sentiment', data=melted_df, palette={'Positive': 'green', 'Negative': 'red', 'Neutral': 'blue'})
plt.title('Average Sentiment Scores During and After the Incident')
plt.xlabel('Time Period')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Sentiment', loc='upper right')
plt.show()
