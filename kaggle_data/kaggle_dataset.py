import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv('avgIQpercountry.csv')
print(data)

last_rows = data.tail(10)
print(last_rows)

data.sample(n=5)
data.sample(frac=0.5)



first_rows = data.head(10)
print(first_rows)

country_data = data['Country']
print(country_data)

subset = data[['Country', 'Average IQ']]
print(subset)

filtered_data = subset[subset['Average IQ'] > 100]
print(filtered_data)

null_mask = data.isnull()
null_count = null_mask.sum()
print("\nCount of null values in each column: ")
print(null_count)

data.dropna(inplace = True)
print("\nDataset information after removing null values")
print(data.info())

duplicated_count = data.duplicated().sum()
print("\nCount of duplicate rows: ")
print(duplicated_count)

data.drop_duplicates(keep='last', inplace=True)

data['Population - 2023'] = data['Population - 2023'].apply(lambda x:float(x.replace(',' , '')))
print(data.info())

#Group by 'Continent' and calculate average IQ
average_iq_per_continent = data.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)

#Sorting the average IQ eper continent in descending order
sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)

#Calculate nobel prices by country
total_nobel_by_country = data.groupby('Country')['Nobel Prices'].sum()
#sort nobel prices in order
sorted_total_nobel_by_country = total_nobel_by_country.sort_values(ascending=False)
print('\nTotal Nobel Prizes by country', sorted_total_nobel_by_country)
sorted_total_nobel_nonzero = sorted_total_nobel_by_country[sorted_total_nobel_by_country !=0]
print("\nTotal Nobel Prizes by Country, excluding countries with zero nobel prizes\n", sorted_total_nobel_nonzero)










