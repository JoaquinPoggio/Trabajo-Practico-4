class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level

class PokemonDatabase:
    def __init__(self):
        self.type_table = {}
        self.number_table = {}
        self.level_table = {}

    def add_pokemon(self, pokemon):
        # Insertar en la tabla de tipos
        for poke_type in pokemon.types:
            if poke_type not in self.type_table:
                self.type_table[poke_type] = []
            self.type_table[poke_type].append(pokemon)
    
        number_key = pokemon.number % 10
        if number_key not in self.number_table:
            self.number_table[number_key] = []
        self.number_table[number_key].append(pokemon)

        level_key = pokemon.level % 10
        if level_key not in self.level_table:
            self.level_table[level_key] = []
        self.level_table[level_key].append(pokemon)
    
    def get_pokemons_with_number_ending(self, digits):
        pokemons = []
        for digit in digits:
            if digit in self.number_table:
                pokemons.extend(self.number_table[digit])
        return pokemons
    
    def get_pokemons_with_level_multiple_of(self, multiples):
        pokemons = []
        for key in self.level_table:
            if any(key % multiple == 0 for multiple in multiples):
                pokemons.extend(self.level_table[key])
        return pokemons
    
    def get_pokemons_of_types(self, types):
        pokemons = []
        for poke_type in types:
            if poke_type in self.type_table:
                pokemons.extend(self.type_table[poke_type])
        return pokemons
    
db = PokemonDatabase()
pokemon1 = Pokemon(23, "Pikachu", ["Electrico"], 15)
pokemon2 = Pokemon(47, "Charmander", ["Fuego"], 20)
pokemon3 = Pokemon(59, "Steelix", ["Acero"], 25)

db.add_pokemon(pokemon1)
db.add_pokemon(pokemon2)
db.add_pokemon(pokemon3)

print("Pokémon cuyos números terminan en 3, 7 y 9:")
for pokemon in db.get_pokemons_with_number_ending([3, 7, 9]):
    print(f"{pokemon.name} (#{pokemon.number})")

print("Pokémon cuyos niveles son múltiplos de 2, 5 y 10:")
for pokemon in db.get_pokemons_with_level_multiple_of([2, 5, 10]):
    print(f"{pokemon.name} (Nivel {pokemon.level})")

print("Pokémon de tipo Acero, Fuego, Electrico, Hielo:")
for pokemon in db.get_pokemons_of_types(["Acero", "Fuego", "Electrico", "Hielo"]):
    print(f"{pokemon.name} (Tipo {', '.join(pokemon.types)})")