#Importando as bibliotecas utilizadas
import pandas as pd
import matplotlib.pyplot as plt

#Lendo o Data Frame 
df_poke_lend = pd.read_csv("pokemon.csv")

#Fazendo o somatório dos lendários, separado pela geração para fazer o comparativo
soma_lendarios_por_geracao = df_poke_lend.groupby('generation')['is_legendary'].sum()

#Laço com print que me trará o resultado para cada ocorrência (geração)
for geracao, soma_lendarios in soma_lendarios_por_geracao.items():
    print("A {}ª geração de Pokémon possui {} pokémons \33[33mLENDÁRIOS\33[0m".format(geracao, soma_lendarios))

#Definição do formato do gráfico
soma_lendarios_por_geracao.plot.bar(x = geracao, y = soma_lendarios)

#Formatando o gráfico
plt.title('Quantidade de Pokémons Lendários em cada Geração')
plt.xlabel("Gerações")
plt.ylabel("Pokémons Lendários")
plt.xticks(rotation = 0)
plt.show()