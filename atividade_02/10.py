df.isnull().sum()

df.dropna()

df.dropna(axis=1)

df.fillna(0)

df['coluna'].fillna(df['coluna'].mean(), inplace=True)

df.fillna(method='ffill')
df.fillna(method='bfill')