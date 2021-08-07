import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_satelites = pd.read_csv('satelites_operando_comercialmente.csv', sep=';')
df_satelites.drop_duplicates(inplace=True)
df_satelites.reset_index(drop=True, inplace=True)

print(df_satelites.info())
df_satelites.head()

# Quantos satélites são brasileiros e quantos são estrangeiro?

plt.figure(figsize=(5,3))
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites, x='Direito')
sns.show()


