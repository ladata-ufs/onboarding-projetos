#Importando as bibliotecas utilizadas
import pandas as pd
import matplotlib.pyplot as plt

#Lendo o Data Frame
df_poke_pow_gen = pd.read_csv("./data/pokemon.csv")

#Ordenando a porcentagem de população masculina de forma decrescente e removendo os casos NULOS, para conseguir separar as populações da melhor maneira.
clasf_gen = df_poke_pow_gen.sort_values('percentage_male', ascending=False, na_position='first').dropna(subset=['percentage_male'], axis='index', ignore_index=True)

#Somátorio do ataque e da defesa para realizar o cálculo da média
soma_ataque = clasf_gen['attack'].sum()
soma_defesa = clasf_gen['defense'].sum()

#Cálculo da média de poder com base no site do BULBAGARDEN https://bulbapedia.bulbagarden.net/wiki/Damage (STAB - TYPE1 - TYPE2 - RANDOM - POWER - CRITICAL foram considerados como 1)
med_poder = (((((2 * 100)/5) + 2) * (clasf_gen['attack'] / clasf_gen['defense'])) / 50) + 2

#Defnição de variável gênero para facilitar a plotagem do gráfico
genero = clasf_gen['percentage_male']

#Definição do formato do gráfico
plt.bar(genero, med_poder, color='blue', label='Poder')

#Formatando o gráfico
plt.xlabel('% Populção Masculina de Pokemons')
plt.ylabel('Poder Médio')
plt.title('Relação entre Poder Médio e Porcentagem de Pokémon Machos')
plt.show()
