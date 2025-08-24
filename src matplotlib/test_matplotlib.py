import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# simple line plot
years = [2018, 2019, 2020, 2021]
temps = [30, 31, 29, 32]

plt.plot(years, temps, marker='o')
plt.xlabel('Year')
plt.ylabel('Average Temp (C)')
plt.title('Yealy Average Temperature')
plt.show()

data = {
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai'],
    'Temp': [32, 30, 28, 35],
    'Humidity': [70, 80, 65, 75]
}
df = pd.DataFrame(data)

# Seaborn Barplot
sns.barplot(x='City', y='Temp', data=df)
plt.show()