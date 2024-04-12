import pandas as pd

df = pd.read_csv('Animation.csv', sep=',')

print(df.head(4))

df.iat[0, 1] = None
df.iat[1, 0] = None
df.iat[2, 3] = None

print(df.head(4))

#print(df.dropna().head(4))  #Вывод без None

print(df.describe())