import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load the dataset using pd.read_excel for Excel files
df = pd.read_excel(r"C:\Users\SATRUC\Documents\globalterrorism.xlsx")

# Displaying first few rows of the dataset
print(df.head())

# Getting information from dataset
print(df.info())

# Describing the data to get statistical summaries
print(df.describe())
# Removing unnecessary columns
df = df[['eventid', 'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city', 'latitude', 'longitude', 'attacktype1_txt', 'targtype1_txt', 'weaptype1_txt', 'nkill', 'nwound', 'summary']]

# Handling missing values
df['nkill'].fillna(0, inplace=True)
df['nwound'].fillna(0, inplace=True)
df.dropna(subset=['latitude', 'longitude'], inplace=True)

# Plotting the top 10 countries with the most terrorist attacks
top_countries = df['country_txt'].value_counts().head(10)
plt.figure(figsize=(15, 6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries with Most Terrorist Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Country')
plt.show()
# Plotting the number of attacks per year
attacks_per_year = df['iyear'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x=attacks_per_year.index, y=attacks_per_year.values)
plt.title('Number of Terrorist Attacks Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.show()
# Plotting the distribution of attack types
attack_types = df['attacktype1_txt'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=attack_types.values, y=attack_types.index)
plt.title('Distribution of Attack Types')
plt.xlabel('Number of Attacks')
plt.ylabel('Attack Type')
plt.show()
