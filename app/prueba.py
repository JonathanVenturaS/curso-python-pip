import pandas as pd

df = pd.read_csv('data.csv')
df = df[df['Continent']== 'South America']

print("Si jala")