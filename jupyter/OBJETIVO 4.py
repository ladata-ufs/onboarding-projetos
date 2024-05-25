#Importando as bibliotecas utilizadas
import pandas as pd
import matplotlib.pyplot as plt

#Lendo o Data Frame
df_poke_pow_gen = pd.read_csv("pokemon.csv")

#Ordenando a porcentagem de população masculina de forma decrescente e removendo os casos NULOS, para conseguir separar as populações da melhor maneira.
clasf_gen = df_poke_pow_gen.sort_values('percentage_male', ascending=False, na_position='first').dropna(subset=['percentage_male'], axis='index', ignore_index=True)

#Cálculo do poder de cada pokémon com base no site do BULBAGARDEN https://bulbapedia.bulbagarden.net/wiki/Damage (STAB - TYPE1 - TYPE2 - RANDOM - POWER - CRITICAL foram considerados como 1)
poder_poke = (((((2 * 100)/5) + 2) * (clasf_gen['attack'] / clasf_gen['defense'])) / 50) + 2

#Defnição de variável gênero para facilitar a plotagem do gráfico
genero = clasf_gen['percentage_male']

# Comparar o poder de cada Pokémon com a média
media_poder = poder_poke.mean()
poder_acima_media = poder_poke > media_poder
poder_abaixo_media = poder_poke < media_poder

# Plotar os resultados
plt.figure(figsize=(10, 6))

plt.bar(genero[poder_acima_media], poder_poke[poder_acima_media], color='blue', label='Acima da Média')
plt.bar(genero[poder_abaixo_media], poder_poke[poder_abaixo_media], color='red', label='Abaixo da Média')

plt.axhline(y=media_poder, color='gray', linestyle='--', label='Média de Poder')

plt.xlabel('% População Masculina de Pokémon')
plt.ylabel('Poder Médio')
plt.title('Relação entre Poder Médio e Porcentagem de Pokémon Machos')
plt.legend()
plt.show()
