from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subscription = \
            [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]
        current_customer = [customer for customer in self.customers if customer.id == current_subscription.customer_id][
            0]
        current_trainer = [trainer for trainer in self.trainers if trainer.id == current_subscription.trainer_id][0]
        current_plan = [plan for plan in self.plans if plan.id == current_subscription.exercise_id][0]
        current_equipment = [equipment for equipment in self.equipment if equipment.id == current_subscription.exercise_id][0]
        result = f"{current_subscription.__repr__()}\n{current_customer.__repr__()}\n{current_trainer.__repr__()}\n" \
                 f"{current_equipment.__repr__()}\n{current_plan.__repr__()}"

        return result



