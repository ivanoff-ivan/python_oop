from pokemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name in [x.name for x in self.pokemon]:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemons:
            self.pokemon.remove(pokemons[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        text = f"Pokemon Trainer {self.name}\n"
        text += f"Pokemon count {len(self.pokemon)}\n"
        for creature in self.pokemon:
            text += "- " + creature.pokemon_details() + "\n"
        return text

