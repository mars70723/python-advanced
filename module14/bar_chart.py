import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

from kaggle_data.kaggle_dataset import filtered_data

df = pd.read_csv('avgIQpercountry.csv')
filtered_df = df[df['Average IQ'] >= 100]
filtered_df = filtered_df.sort_values(by = 'Average IQ', ascending=False)
print(filtered_df)

#Create a figure for the bar chart with a specified size
plt.figure(figsize=(14,8))
bars = plt.bar(filtered_df["Country"], filtered_data["Average IQ"], color="skyblue")
plt.title("Average IQ by country (IQ >= 100)", fontsize=16)
#Add labels to the x-axis and y-axis
plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

#Rotate the x-axis labels for better readability
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

#Add gridlines to the y-axis for the better readability
plt.grid(axis='y', linestyles='--', alpha=0.8)

#Add text labels
plt.bar_label(bars, fat='%.2f', fontsize=10, color='black')

plt.tight_layout()
plt.show()

