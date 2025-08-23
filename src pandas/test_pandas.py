# import numpy as np
import pandas as pd

# s = pd.Series(data, index=index)

# Create dataframe
data = {
    'City' : ['Delhi', 'Mumbai', 'Bangalore', 'Chennai'],
    'Temp' : [32, 30, 26, 35],
    'Humidity' : [70, 80, 60, 75]
}
df = pd.DataFrame(data)

# Indexing
print(df['Temp'])    # column select
print(df.loc[0])     # row select by index
print(df.iloc[2])    # row select by position

# Filtering
print(df[df['Temp'] > 30])    # rows where temp > 30

# GroupBy
grouped = df.groupby('City')['Humidity'].mean()
print(grouped)

# Joining
df2 = pd.DataFrame({'City': ['Delhi', 'Mumbai'], 'AQI' : [120, 150]})
merged = pd.merge(df, df2, on='City', how='left')
print(merged)
