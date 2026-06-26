import json
import os

# File that will store all Pokémon
FILE_NAME = "pokemon.json"

# Starter Pokémon (used only the very first time)
INITIAL_DATA = [
    {
        "name": {"english": "Pikachu"},
        "type": ["Electric"],
        "base": {"HP": 35, "Attack": 55, "Defense": 40, "Sp. Attack": 50, "Sp. Defense": 50, "Speed": 90}
    },
    {
        "name": {"english": "Charmander"},
        "type": ["Fire"],
        "base": {"HP": 39, "Attack": 52, "Defense": 43, "Sp. Attack": 60, "Sp. Defense": 50, "Speed": 65}
    },
    {
        "name": {"english": "Squirtle"},
        "type": ["Water"],
        "base": {"HP": 44, "Attack": 48, "Defense": 65, "Sp. Attack": 50, "Sp. Defense": 64, "Speed": 43}
    }
]

def load_pokemons():
    """Load Pokémon list. Creates the file with starters if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        print(f"File '{FILE_NAME}' not found → creating it with the 3 starters!")
        save_pokemons(INITIAL_DATA)
        return INITIAL_DATA.copy()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Loaded {len(data)} Pokémon!")
            return data
    except json.JSONDecodeError:
        print("JSON file is broken → starting with an empty list.")
        return []

def save_pokemons(pokemons):
    """Save the full list back to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(pokemons, f, indent=2, ensure_ascii=False)
    print(f"Data saved to '{FILE_NAME}'")

def ask_number(prompt):
    """Ask for an integer with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a whole number.")

def add_pokemon():
    """Ask the user for a new Pokémon and append it."""
    pokemons = load_pokemons()

    print("\n" + "="*44)
    print("       ADD A NEW POKÉMON")
    print("="*44)

    # ---- Name ----
    name = input("\nEnglish name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    # ---- Types ----
    types_input = input("Types (comma-separated, e.g. Fire, Flying): ").strip()
    types = [t.strip().capitalize() for t in types_input.split(",") if t.strip()]
    if not types:
        types = ["Normal"]
        print("No type entered → assigned 'Normal'")

    # ---- Base Stats ----
    print("\n--- Base Stats ---")
    hp        = ask_number("HP: ")
    attack    = ask_number("Attack: ")
    defense   = ask_number("Defense: ")
    sp_attack = ask_number("Sp. Attack: ")
    sp_def    = ask_number("Sp. Defense: ")
    speed     = ask_number("Speed: ")

    # ---- Build the new Pokémon ----
    new_pokemon = {
        "name": {"english": name},
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_def,
            "Speed": speed
        }
    }

    # ---- Save ----
    pokemons.append(new_pokemon)
    save_pokemons(pokemons)

    # ---- Confirmation ----
    print("\nPokémon added!")
    print(f"Name: {name}")
    print(f"Types: {', '.join(types)}")
    print(f"HP: {hp} | Speed: {speed}")

# ─────────────────────────────────────
if __name__ == "__main__":
    add_pokemon()
    print("\nAll done! Open 'pokemon.json' to see every Pokémon.")