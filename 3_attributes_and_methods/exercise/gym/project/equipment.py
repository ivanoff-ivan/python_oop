class Equipment:
    id_generator = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.id_generator += 1
        return Equipment.id_generator

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


