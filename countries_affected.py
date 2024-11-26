import requests
from bs4 import BeautifulSoup
import plotly.express as px

# Step 1: Extract and categorize the countries
url = "https://www.timesnownews.com/world/microsoft-outage-here-are-20-most-affected-countries-article-111874112"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Extract the countries
affected_countries = soup.find_all("li")
# print(affected_countries)
# Categorize the countries
most_affected = [
    'United States', 'United Kingdom', 'Canada'
]  # Add countries you consider most affected
less_affected = [
    'Australia', 'Germany', 'France', 'India'
]  # Add countries you consider less affected
slightly_affected = [
    'Spain', 'Italy', 'Netherlands', 'Sweden', 'Denmark', 'Norway', 'Finland',
    'Belgium', 'Switzerland', 'Austria', 'Ireland', 'Portugal', 'New Zealand'
]  # Add countries you consider slightly affected

categories = []

countries = []

for country in affected_countries:
    strong_tag = country.find("strong")
    if strong_tag is not None:
        country_name = strong_tag.text
        if country_name in most_affected:
            categories.append('Most Affected')
            countries.append(country_name)
        elif country_name in less_affected:
            categories.append('Less Affected')
            countries.append(country_name)
        elif country_name in slightly_affected:
            categories.append('Slightly Affected')
            countries.append(country_name)

# Step 2: Prepare data for visualization
data = {'Country': countries, 'Category': categories}
print(data)
# Step 3: Create the map visualization
# Create a numerical mapping for the categories
category_to_value = {
    'Most Affected': 3,
    'Less Affected': 2,
    'Slightly Affected': 1
}
data['Value'] = [category_to_value[cat] for cat in data['Category']]

# Convert data to DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create the choropleth map using Plotly
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

# Show the figure
fig.show()
# Step 4: Save Data to CSV
csv_filename = 'affected_countries.csv'
df.to_csv(csv_filename, index=False)