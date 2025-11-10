import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
   url = f"{base_url}/pokemon/{name}"
   response = requests.get(url)
   print(response) #status code <200>

   if response.status_code == 200:
      print("Data retrieved!")
      pokemon_data=response.json() #convert to dict form
      return pokemon_data
      print(pokemon_data)
      pass
   else:
      print(f"Failed to retrieve data {response.status_code}")
 
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
   print(f"Name: {pokemon_info["name"]}")
   print(f"Id: {pokemon_info["id"]}")
   print(f"Height: {pokemon_info["height"]}")
   