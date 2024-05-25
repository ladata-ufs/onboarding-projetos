import pandas as pd
import matplotlib.pyplot as plt

# Read csv and turning into pandas object
df_pokemon = pd.read_csv('./data/pokemon.csv')

# Define power stats trying to follow the stats applied in the game
# src: https://bulbapedia.bulbagarden.net/wiki/Damage
# Define some medias to grow the accuracy of selection of the most powerful pokemons
poke_def_media = df_pokemon['defense'].median() + df_pokemon['sp_defense'].median()
poke_power_media = 100
poke_level = 100
# Add new columns which will help to get a more accuracy selection
df_pokemon['attack_power'] = df_pokemon['attack'] + df_pokemon['sp_attack']
df_pokemon['power_stat'] = (((2 * poke_level) / 5 + 2) *
                            poke_power_media *
                            (df_pokemon['attack_power'] / poke_def_media)) / 50 + 2


# Ordering the Pokemons by power stats
df_pokemon = df_pokemon.sort_values(
    by=['power_stat'],
    ascending=[False],
    kind='quicksort'
)

# Initilize library config to plot result
plt.figure()

# Get the top 100 most powerful
df_resumed = df_pokemon[['abilities', 'classfication', 'type1', 'type2', 'generation']].head(100)

# Initializing dictionaries that will be used to store the target information and reducing the scope
classification = {}
pokemon_type = {}
generation = {}
abilities = {}

# ABILITIES counting
for index, row in df_resumed.iterrows():
    # Obtaining abilities of each Pokemon
    pokemon_abilities = row['abilities'].strip('][').split(', ')
    # Making the sum
    for pokemon_ability in pokemon_abilities:
        if pokemon_ability in abilities.keys():
            abilities[pokemon_ability] = abilities[pokemon_ability] + 1
            continue
        abilities[pokemon_ability] = 1
# Converting and ordering obtained data
abilities = dict(sorted(abilities.items(), key=lambda item: item[1], reverse=True))
top_abilities = pd.DataFrame(list(abilities.items()), columns=['ability', 'amount'])
top_abilities = top_abilities.head(5)

# Plot results
ax = top_abilities.plot.bar(x='ability', y='amount', rot=0)

# GENERATION counting
for index, row in df_resumed.iterrows():
    # Obtaining abilities of each Pokemon
    pokemon_generation = row['generation']
    # Making the sum
    if pokemon_generation in generation.keys():
        generation[pokemon_generation] = generation[pokemon_generation] + 1
        continue
    generation[pokemon_generation] = 1
# Converting and ordering obtained data
generation = dict(sorted(generation.items(), key=lambda item: item[1], reverse=True))
gen_amount = pd.DataFrame(list(generation.items()), columns=['generation', 'amount'])
# Plot results
ax = gen_amount.plot.bar(x='generation', y='amount', rot=0)
# print(gen_amount.to_string())

# TYPE counting
for index, row in df_resumed.iterrows():
    # Obtaining types of each Pokemon
    poke_type1 = row['type1']
    poke_type2 = row['type2']
    # Making the sum
    if poke_type1 in pokemon_type.keys():
        pokemon_type[poke_type1] = pokemon_type[poke_type1] + 1
        continue
    pokemon_type[poke_type1] = 1
    if poke_type2 in pokemon_type.keys():
        pokemon_type[poke_type2] = pokemon_type[poke_type2] + 1
        continue
    pokemon_type[poke_type2] = 1
# Converting and ordering obtained data
pokemon_type = dict(sorted(pokemon_type.items(), key=lambda item: item[1], reverse=True))
poke_type_amount = pd.DataFrame(list(pokemon_type.items()), columns=['type', 'amount'])
# Plot result
ax = gen_amount.plot.bar(x='type', y='amount', rot=0)
# print(poke_type_amount.to_string())

# CLASSFICATION counting
for index, row in df_resumed.iterrows():
    # Obtaining classification of each Pokemon
    pokemon_class = row['classfication']
    # Verifying if a pokemon classification already exists in list
    if pokemon_class in classification.keys():
        classification[pokemon_class] = classification[pokemon_class] + 1
        continue
    classification[pokemon_class] = 1
# Converting and ordering obtained data
classification = dict(sorted(classification.items(), key=lambda item: item[1], reverse=True))
poke_class_amount = pd.DataFrame(list(classification.items()), columns=['classfication', 'amount'])
# Plot result
ax = gen_amount.plot.bar(x='classfication', y='amount', rot=0)
# print(poke_class_amount.to_string())
