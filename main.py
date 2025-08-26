import requests

# pokemon API base url
base_url = "https://pokeapi.co/api/v2/"

def menu():
  print("------------------------")
  print("\n Welcome to the pyDex\n")
  print("(1) Search for a Pokemon\n")
  print("(2) Assemble Party\n")
  print("(3) Surprise me!\n")
  print("------------------------")

pokemon_party = []
pokemon_party_size = 6

def main():
  menu()
  menu_selection = int(input("To access - Select from 1 to 3: "))


  if menu_selection == 1:
    search()
  elif menu_selection == 2:
    party()
  elif menu_selection == 3:
    surprise()
  else:
    return



def party():
    for poke in range(7):
        pokemon_entry: str = input("Add a Pokemon to your party (Name or ID): ")
        pokemon_party.append(pokemon_entry)
        print(pokemon_entry)

    if poke == pokemon_party_size:
      print("Your party is assembled: ")
      print(pokemon_party)
    else:
        print("Can't find pokemon in pyDex")
        print("\n")

def surprise():
  print("\n")
  print("Surprise!")


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print("Failed to retrieve data!")




def search():
    pokemon_name = input("Enter the pokemon's name: ")
    print("\n")
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"Id: {pokemon_info["id"]}")
        print(f"Type: {pokemon_info['types']}")
        print(f"Height: {pokemon_info["height"]}")
        print(f"Weight: {pokemon_info["weight"]}")

def go_back():
    menu()


# call main function
main()
