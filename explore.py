#Self Assessment
#1. What the boolean filter does is it gives true or false values for each row inside of the dataframe.
#2. The single bracket gives gives a series while the double bracket gives a dataframe. What this means
# is that the single bracket will return a single column while the double bracket will return multiple columns.
#3. The code becomes repeatable using pandas, so you are able to implement it into real work by reusing it and rerunning it a day, or month later.
#It also handles large datasets and can be used to analyze data more efficeintly than excel.

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

print(len(big_south))
print(big_south.head())

# Exercise 5

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6

print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7

subset = df[['region', 'product', 'revenue']]
print(subset.shape)

# Exercise 8

df.to_csv('data/explored.csv', index=False)
