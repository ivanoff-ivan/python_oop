from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            current_worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_needs = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= sum_of_needs:
            self.__budget -= sum_of_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_list = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers_list = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs_list = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions_list)} Lions:\n"
        result += '\n'.join(['' + lion.__repr__() for lion in lions_list])
        result += f"\n"
        result += f"----- {len(tigers_list)} Tigers:\n"
        result += '\n'.join([tiger.__repr__() for tiger in tigers_list])
        result += f"\n"
        result += f"----- {len(cheetahs_list)} Cheetahs:\n"
        result += '\n'.join([cheetah.__repr__() for cheetah in cheetahs_list])
        return result

    def workers_status(self):
        keepers_list = [keeper for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        caretakers_list = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == "Caretaker"]
        vets_list = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers_list)} Keepers:\n"
        result += '\n'.join([k.__repr__() for k in keepers_list])
        result += "\n"
        result += f"----- {len(caretakers_list)} Caretakers:\n"
        result += '\n'.join([c.__repr__() for c in caretakers_list])
        result += "\n"
        result += f"----- {len(vets_list)} Vets:\n"
        result += '\n'.join([v.__repr__() for v in vets_list])
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
