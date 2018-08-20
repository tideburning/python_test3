import pandas as pd 
#read data from csv file
data_pokemons = pd.read_csv("pokemon.csv") 

#print(type(data_pokemons))
#print (data_pokemons.columns)

#find the pokemons with speed > 80 and attack >52
res = data_pokemons[(data_pokemons['Speed'] >80) & (data_pokemons['Attack'] > 52)]
print(res)

#draw res
import matplotlib.pyplot as plt
plt.plot(res['Speed'] , color= "r", label = 'speed')
plt.plot(res['Attack'], color= "b", label = 'attack')
#show legend
plt.legend()
plt.show()