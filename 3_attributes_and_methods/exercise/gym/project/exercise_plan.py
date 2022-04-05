class ExercisePlan:
    id_generator = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, duration: int):
        return cls(trainer_id, equipment_id, duration * 60)

    @staticmethod
    def get_next_id():
        ExercisePlan.id_generator += 1
        return ExercisePlan.id_generator

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
