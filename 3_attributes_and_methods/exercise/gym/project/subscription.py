class Subscription:
    id_generator = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Subscription.id_generator += 1
        return Subscription.id_generator

    def __repr__(self):
        info = f"Subscription <{self.id}> on {self.date}"
        return info
