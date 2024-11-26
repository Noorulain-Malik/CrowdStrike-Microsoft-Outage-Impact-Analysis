import os
import pandas as pd
import csv as csv

source_file="C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Microsoft_outage\\lossdata.csv" 
df = pd.read_csv(source_file)

# Check if the file exists
print(df)