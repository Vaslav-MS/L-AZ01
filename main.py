import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

print(df.head())
print(df.info())
print(df.describe())

dz = pd.read_csv('dz.csv')

group = dz.groupby('City')['Salary'].mean()

print('Средние зарплаты по городам:')
print(group)
