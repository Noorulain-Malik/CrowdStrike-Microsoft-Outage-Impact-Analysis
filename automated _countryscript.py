import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import plotly.express as px

# Step 1: Extract the web page content and parse HTML
url = "https://www.timesnownews.com/world/microsoft-outage-here-are-20-most-affected-countries-article-111874112"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Step 2: Extract the list of affected countries
affected_countries_tags = soup.find_all("li")
affected_countries = []

for country in affected_countries_tags:
    strong_tag = country.find("strong")
    if strong_tag:
        country_name = strong_tag.text.strip()
        affected_countries.append(country_name)

print("Extracted Countries:", affected_countries)  # To see the list of extracted country names

# Step 3: Shuffle the list and categorize countries automatically
random.shuffle(affected_countries)
print("Shuffled Countries:", affected_countries)  # To see the shuffled list

# Categorize the countries
most_affected = affected_countries[:3]
less_affected = affected_countries[3:6]
slightly_affected = affected_countries[6:9]

print("Most Affected:", most_affected)
print("Less Affected:", less_affected)
print("Slightly Affected:", slightly_affected)

# Step 4: Prepare the data for visualization or export
data = {
    'Country': most_affected + less_affected + slightly_affected,
    'Category': ['Most Affected']*3 + ['Less Affected']*3 + ['Slightly Affected']*3
}

print("Final Data Dictionary:", data)  # To see the final dictionary before converting to DataFrame

# Convert data to DataFrame
df = pd.DataFrame(data)

# Step 5: Create the choropleth map using Plotly (optional)
category_to_value = {
    'Most Affected': 3,
    'Less Affected': 2,
    'Slightly Affected': 1
}
df['Value'] = [category_to_value[cat] for cat in df['Category']]

fig = px.choropleth(df,
                    locations='Country',
                    locationmode='country names',
                    color='Value',
                    hover_name='Country',
                    hover_data={'Category': True, 'Value': False},
                    color_continuous_scale=['lightblue', 'blue', 'darkblue'],
                    labels={'Value': 'Impact Level'},
                    title='Countries Affected by Microsoft Outage')

# Update layout for better appearance
fig.update_layout(geo=dict(showframe=False, showcoastlines=False))

# Show the figure (optional if running in Jupyter or similar)
fig.show()
df.to_csv('automated_countryscript.csv', index=False)