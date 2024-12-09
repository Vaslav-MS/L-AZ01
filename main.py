import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
gh = pd.read_csv('products.csv', sep=';')

print(gh.info())
