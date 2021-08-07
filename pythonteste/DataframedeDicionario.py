import pandas as pd
dados = {'nomes':'Howard Ian Peter Jonah Kellie'.split(),
         'cpfs': '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
         'emails':'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
         'idades':[32,22,25,29,38],
         }
df_dados = pd.DataFrame(dados)
print(df_dados)
print('--------------------------------------')
print('\n Informações do DataFrame: \n')
print(df_dados.info())
print('\nQuantidade de linhas e colunas:\n', df_dados.shape)
print('\nTipos de dados:\n', df_dados.dtypes)
print('\nQual é o menor valor de cada coluna:\n',df_dados.min())
print('\nQual é o maior valor de cada coluna:\n',df_dados.max())
print('\nQual é a média aritmética?\n',df_dados.mean())
print('\nQual é o desvio padrão:\n',df_dados.std())
print('\nQual é a mediana?\n',df_dados.median())
print('\nResumo\n', df_dados.describe())
print('--------------------------------------')
df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print(df_uma_coluna)
print('Media de idades = ',df_uma_coluna.mean())
print('--------------------------------------')
colunas = ['nome','idade']
df_duas_colunas= df_dados[colunas]

