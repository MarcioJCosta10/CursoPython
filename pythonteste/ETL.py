import requests
# exibindo o primeiro registro de dados (primeiro dicionário da lista
dados = requests.get('https://servicodados.ibge.gov.br/api/v2/cnae/classes').json()

# Quantidade distintas de atividades, basta saber o tamanho da lista.
dados [0]
qtde_atividades_distintas = len(dados)


# Criar uma lista dos grupos de atividades, extraindo a descrição de cada registro
grupos = []
for registro in dados:
    grupos.append(registro['grupo']['descricao'])
grupos[:10]
# A partir da lista, podemos extrair a quantidade de grupos de atividades
qtde_grupos_distintos = len(set(grupos))  # o construtor set cria uma estrutura de dados removendo as duplicações.

grupos_count = [(grupo, grupos.count(grupo))for grupo in set(grupos)]
grupos_count[:5]

# Por conveniência, transformamos a lista em um dicionário
grupos_count = dict(grupos_count)

valor_maximo = max(grupos_count.values())
grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]
print(f'O grupo que tem mais atividades é o grupo: ', len(grupos_mais_atividades))
grupos_mais_atividades






