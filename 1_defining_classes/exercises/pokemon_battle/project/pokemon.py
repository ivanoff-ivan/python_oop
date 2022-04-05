from pokemon_battle.project.trainer import Trainer

class Pokemon:
    def __init__(self, name, health: int):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"