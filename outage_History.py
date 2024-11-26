import os 

import pandas as pd,openpyxl 
import xlrd as xlrd
from io import StringIO


# Cleaned CSV data
csv_data_clean = """Outage Name,Year,Devices/Users Affected,Sectors Impacted,Specific Disruptions,Financial Loss
CrowdStrike Incident,2024,8.5M devices,"Airlines, Media, Healthcare, Financial Services","Over 2,000 flight cancellations, media downtime, delays in healthcare and banking services","Estimated up to $5.4B for top 500 US companies"
Azure Service Disruption,2023,Hundreds of customers,"Various industries relying on Azure services","Service disruptions in Azure SQL DB, Cosmos DB, VM availability","Not specified"
Office 365 Outage,2022,Millions of users,"Businesses, Educational Institutions, Government","Email, Teams, and other Office 365 services unavailable","Not specified"
Azure Active Directory Outage,2021,Global impact,"Any service dependent on Azure AD for authentication","Authentication issues across multiple services","Not specified"
Exchange Online Outage,2020,Millions of users,"Businesses, Educational Institutions, Government","Email services disrupted","Not specified"
Teams Outage,2019,Millions of users,"Businesses, Educational Institutions, Remote Workers","Microsoft Teams unavailable for several hours","Not specified"
"""

# Use StringIO to simulate reading from a file
data_clean = StringIO(csv_data_clean)

# Create a DataFrame
df = pd.read_csv(data_clean)
print(df)
# print(df.columns)
df.to_excel("outage_history.xlsx",index=False)