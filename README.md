
![Screenshot 2024-11-26 012850](https://github.com/user-attachments/assets/de09b1af-3b9c-469a-a393-0154700d6224)


# CrowdStrike Incident & Microsoft Outage Impact Analysis

This analysis not only sheds light on the **CrowdStrike incident** but also offers a framework for understanding the economic and societal impacts of large-scale **cybersecurity events**. Whether you're in **cybersecurity**, **finance**, or just passionate about tech, this project helps to visualize and quantify the scale of such events. The combination of **historical context**, **sentiment analysis**, and **financial loss estimates** makes it a comprehensive resource for understanding the implications of major disruptions in global services.

## Overview

This project provides an in-depth analysis of the **CrowdStrike incident** and the **Microsoft outage** that occurred in **July 2024**, impacting various industries. Through a combination of **web scraping**, **sentiment analysis**, and **financial loss estimation**, this analysis provides insights into how the incident affected companies globally. The project includes sentiment analysis of **Reddit** discussions, visualization of the financial losses, categorization of the **most affected countries**, and a historical comparison of similar outages. 
Interactive visualizations have been created to display key trends and impacts, including **Power BI dashboards** and **Plotly maps**. The findings offer a comprehensive view of the cyber incident’s effects on the global tech and cybersecurity landscape.

## Key Features

- **Sentiment Analysis**: Performed on **Reddit posts and comments** using **VADER Sentiment Analysis**, providing insights into public perception before, during, and after the CrowdStrike incident.![Screenshot 2024-11-26 014224](https://github.com/user-attachments/assets/24e60671-c87f-47e7-a109-5b4038a7f78e)
![Screenshot 2024-11-26 014153](https://github.com/user-attachments/assets/058d7afd-ab3a-4e40-85e8-cd33d9a986f0)
![Screenshot 2024-11-26 021001](https://github.com/user-attachments/assets/3a2fdb67-0dd4-4ece-bade-46b41e38f002)

- **Web Scraping**: Utilized **BeautifulSoup** and **requests** to scrape **affected country information** from **Times Now News**.![Screenshot 2024-11-26 013936](https://github.com/user-attachments/assets/3b945227-5c96-44b2-ac0e-6a92cbae411e) ![Screenshot 2024-11-26 014132](https://github.com/user-attachments/assets/5edbcd83-e2e8-4077-ab43-654919f4cd35)


- **Data Collection & Cleaning**: Scrapes **Reddit** data and categorizes **airline-related posts** and **comments** using predefined keywords.
- **Financial Loss Estimation**: Estimates the financial impact of the CrowdStrike incident, calculating up to **$5.4 billion** in losses for the top 500 U.S. companies.![Screenshot 2024-11-26 014011](https://github.com/user-attachments/assets/7deccc80-ff29-4609-99e6-beb72f66477e)

- **Affected Country Categorization**: Scrapes and categorizes **20 affected countries** into **Most Affected**, **Less Affected**, and **Slightly Affected**, visualized using **interactive choropleth maps**.![Screenshot 2024-11-26 014041](https://github.com/user-attachments/assets/7c0e0094-7e48-45d5-93df-2408918bef77)

- **Historical Outage Data**: Provides context on previous similar outages, comparing the **CrowdStrike incident** with past disruptions.
- **Visualization**: Uses **Power BI** and **Plotly** to generate **interactive dashboards** and **choropleth maps** to visualize sentiment trends, financial loss, and the global impact of the incident.

![Screenshot 2024-11-26 015714](https://github.com/user-attachments/assets/c00c7f53-b71f-4ee0-989a-23f41f39fe62)
![Screenshot 2024-11-26 020024](https://github.com/user-attachments/assets/ec3e4bab-c922-4621-8b7f-da957cc24997)
## Technologies Used

- **Python**: Core scripting language for data collection, cleaning, and analysis.
  - Libraries: `pandas`, `matplotlib`, `seaborn`, `plotly`, `requests`, `beautifulsoup4`, `vaderSentiment`
- **Power BI**: Used to create **interactive dashboards** to visualize sentiment trends, financial loss, and the affected regions.
- **Plotly**: For creating **interactive choropleth maps** to visualize the severity of the incident across different countries.
- **Web Scraping**: Used **BeautifulSoup** and **requests** to extract relevant data from external websites.
- **VADER Sentiment Analysis**: Applied for sentiment scoring on **Reddit** posts and comments to understand public reactions to the outage.

## Project Structure

```
Crowdstrike-Microsoft-Outage-Impact-Analysis/
│
├── data/                                # Data files (.csv, .xlsx)
│   ├── lossdata.csv                    # Financial loss data
│   ├── affected_countries.csv          # Affected countries categorized
│   ├── outage_history.xlsx             # Historical outage details
│
├── scripts/                             # Python scripts for analysis
│   ├── loss.py                         # Financial loss estimation script
│   ├── automated_countryscript.py      # Scrapes and categorizes affected countries
│   ├── countries_affected.py           # Categorizes and maps affected countries
│   ├── outage_history.py               # Historical outage data
│   ├── sentiment_analysis.py           # Sentiment analysis on Reddit posts
│
├── visualizations/                     # Exported visualizations
│   ├── crowdstrike_incident.pbix       # Power BI dashboard file
│
└── README.md                           # Project documentation
```

## Results

- **Countries Affected**: The choropleth map visualizes how the outage impacted **20 countries** with varying levels of severity, from **Most Affected** to **Slightly Affected**.
- **Sentiment Trends**: Public sentiment trends are visualized through interactive dashboards, showing how **Reddit discussions** changed from **negative** to **neutral/positive** during and after the incident.
- **Financial Loss**: The financial loss due to the outage is estimated, with the **CrowdStrike incident** resulting in up to **$5.4 billion** in losses for the top 500 U.S. companies.
- **Historical Context**: A deep dive into historical outages, comparing CrowdStrike with similar disruptions, helps contextualize the scale and impact of the event.


## Future Work

- Expand the sentiment analysis to **Twitter** and other social media platforms.
- Integrate more granular financial metrics and explore the **long-term impact** on affected sectors.
- Include more **cybersecurity companies** for a comparative analysis of industry responses to the outage.


[Crowdstrike.pptx](https://github.com/user-attachments/files/17913932/Crowdstrike.pptx)





