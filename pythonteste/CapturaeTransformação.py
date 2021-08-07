import pandas as pd
from datetime import date
from datetime import datetime as dt
import parser
df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
print(df_selic.info())
df_selic.drop_duplicates(keep='last',inplace=True)
print(df_selic)
# CRIAR NOVAS COLUNAS
data_extracao = date.today()
df_selic['data_extracao']= data_extracao
df_selic['responsavel']='Autora'

print(df_selic.info())
df_selic.head()

df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')
print(df_selic.info())
df_selic.head()

df_selic['reponsavel'] = df_selic['responsavel'].str.upper()
df_selic.head()

df_selic.sort_values(by='data', ascending=False, inplace=True)
df_selic.head()

df_selic.reset_index(drop=True, inplace=True) #(drop=True), diz que não queremos usar o índice que será substituído em uma nova coluna
df_selic.head()

# pode ser necessário definir novos valores para os índices, ao invés de usar o range numérico
lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
print(lista_novo_indice[:5])
df_selic.set_index(keys=[lista_novo_indice], inplace=True)
df_selic.head()
print(df_selic)

# descobrir qual o índice do menor e do maior de uma Series
print('Menor indice da serie',df_selic['valor'].idxmin())
print('Maior indice da serie',df_selic['valor'].idxmax())

# Essa propriedade permite acessar um conjunto de linhas
selic_indice1 = df_selic.loc['selic_1']
print('O selic_indice0 é:',selic_indice1)

# foram filtrados três registros, para isso foi necessário passar uma lista contendo os índices, como resultado obtivemos um novo DF
todosdados = df_selic.loc[['selic_0','selic_1','selic_2','selic_3']]
print(todosdados)
cincoprimeiros=df_selic.loc[:'selic_5']
print(cincoprimeiros)

filtroecoluna=df_selic.loc[['selic_0','selic_4','selic_200']]['valor']
print('O filtro e uma coluna:',filtroecoluna)
filtroecolunas=df_selic.loc[['selic_0','selic_4','selic_200']][['valor','data_extracao']]
print('O filtro e varias colunas:','\n',filtroecolunas)


# iloc, a qual filtra as linhas considerando a posição que ocupam no objeto.
testecomILOC=df_selic.iloc[:5]
print('O teste com iloc é:',testecomILOC)

testebooleano = df_selic['valor'] < 0.01
testebooleano.head()
print('O teste boleano é','\n',testebooleano)

# o método to_datetime() para converter a string para data e então fazer a comparação
testeboleano2 = df_selic['data'] >= pd.to_datetime('2020-01-01')
print('O testebooleano2 é:',testeboleano2)

# O teste condicional pode ser construído também utilizando operadores lógicos
testebooleano3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))
testebooleano4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))
print(testebooleano4)
print("Resultado do AND:\n")
print(testebooleano3[:3])
print("Resultado do OR:\n")
print(testebooleano4[:3])

# Após criadas as condições, basta aplicá-las no DataFrame para criar o filtro. A construção é feita passando a condição para a propriedade loc.

filtro1 = df_selic['valor'] < 0.01
testefiltro=df_selic.loc[filtro1]
print('O teste do filtro é:',testefiltro)

data1 = pd.to_datetime('2020-01-01')
data2 = pd.to_datetime('2020-01-31')
filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
df_janeiro_2020.head()
print(df_janeiro_2020)

data3 = pd.to_datetime('2019-01-01')
data4 = pd.to_datetime('2019-01-31')
filtro_janeiro_2019 = (df_selic['data'] >= data3) & (df_selic['data'] <= data4)
df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
df_janeiro_2019.head()
print(df_janeiro_2019)





















































