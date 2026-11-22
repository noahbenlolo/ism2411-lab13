# Exercise 1
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

# Exercise 3

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

# Exercise 4

big_south =df[(df['region'] == 'South') & (df['revenue'] > 1000)]

# Exercise 5

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())

# Exercise 6

print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7

subset = df[['region', 'product', 'revenue']]
print(subset.shape)

# Exercise 8

df.to_csv('data/explored.csv', index=False)
