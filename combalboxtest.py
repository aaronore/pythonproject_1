import pandas as pd
 
data = {'owid-co2-data.csv'} 
df = pd.read_csv('owid-co2-data.csv')

df.drop_duplicates(subset=['country'],keep='first',inplace=True)

print(df)