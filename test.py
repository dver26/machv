from src.machv import Dataset
import numpy as np

# formato: [nombre, tipo1, tipo2, hp, attack, defense, sp_atk, sp_def, speed, legendary]
pokemons = [
    ["Bulbasaur",  "Grass",    "Poison",  45,  49,  49,  65,  65,  45, 0],
    ["Ivysaur",    "Grass",    "Poison",  60,  62,  63,  80,  80,  60, 0],
    ["Venusaur",   "Grass",    "Poison",  80,  82,  83, 100, 100,  80, 0],
    ["Charmander", "Fire",     None,      39,  52,  43,  60,  50,  65, 0],
    ["Charmeleon", "Fire",     None,      58,  64,  58,  80,  65,  80, 0],
    ["Charizard",  "Fire",     "Flying",  78,  84,  78, 109,  85, 100, 0],
    ["Squirtle",   "Water",    None,      44,  48,  65,  50,  64,  43, 0],
    ["Wartortle",  "Water",    None,      59,  63,  80,  65,  80,  58, 0],
    ["Blastoise",  "Water",    None,      79,  83, 100,  85, 105,  78, 0],
    ["Pikachu",    "Electric", None,      35,  55,  40,  50,  50,  90, 0],
    ["Raichu",     "Electric", None,      60,  90,  55,  90,  80, 110, 0],
    ["Jigglypuff", "Normal",   "Fairy",  115,  45,  20,  45,  25,  20, 0],
    ["Meowth",     "Normal",   None,      40,  45,  35,  40,  40,  90, 0],
    ["Psyduck",    "Water",    None,      50,  52,  48,  65,  50,  55, 0],
    ["Machop",     "Fighting", None,      70,  80,  50,  35,  35,  35, 0],
    ["Gastly",     "Ghost",    "Poison",  30,  35,  30, 100,  35,  80, 0],
    ["Onix",       "Rock",     "Ground",  35,  45, 160,  30,  45,  70, 0],
    ["Eevee",      "Normal",   None,      55,  55,  50,  45,  65,  55, 0],
    ["Snorlax",    "Normal",   None,     160, 110,  65,  65, 110,  30, 0],
    ["Articuno",   "Ice",      "Flying",  90,  85, 100,  95, 125,  85, 1],
    ["Zapdos",     "Electric", "Flying",  90,  90,  85, 125,  90, 100, 1],
    ["Moltres",    "Fire",     "Flying",  90, 100,  90, 125,  85,  90, 1],
    ["Mewtwo",     "Psychic",  None,     106, 110,  90, 154,  90, 130, 1],
]

names = ["nombre", "tipo1", "tipo2", "hp", "attack", "defense", "sp_atk", "sp_def", "speed", "legendary"]

X = np.array(pokemons)[:, 1:-1]
y = np.array(pokemons)[:, -1]

d = Dataset(X, y, names[1:-1], names[-1])
print(d)

# Característiques del dataset
print("Característiques del dataset")
print("Nombre de mostres: ", len(d))
print("Nombre de característiques: ", d.n_attr())
print("Noms de les característiques: ", d.names)
