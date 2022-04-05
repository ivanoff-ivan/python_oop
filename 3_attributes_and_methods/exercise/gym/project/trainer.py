class Trainer:
    id_generator = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.id_generator += 1
        return Trainer.id_generator

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
