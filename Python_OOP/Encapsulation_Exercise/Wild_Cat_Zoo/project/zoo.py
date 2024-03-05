class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return 'Not enough space for worker'

    def fire_worker(self, worker_name):

        for obj in self.workers:
            if obj.name == worker_name:
                self.workers.remove(obj)
                return f'{worker_name} fired successfully'

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum([obj.salary for obj in self.workers]):
            self.__budget -= sum([obj.salary for obj in self.workers])
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        if self.__budget >= sum([obj.money_for_care for obj in self.animals]):
            self.__budget -= sum([obj.money_for_care for obj in self.animals])
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'

        lions = [obj for obj in self.animals if obj.__class__.__name__ == "Lion"]
        tigers = [obj for obj in self.animals if obj.__class__.__name__ == "Tiger"]
        cheetahs = [obj for obj in self.animals if obj.__class__.__name__ == "Cheetah"]

        result += f'----- {len(lions)} Lions:\n'
        for lion in lions:
            result += f'{lion}\n'

        result += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            result += f'{tiger}\n'

        result += f'----- {len(cheetahs)} Cheetahs:\n'
        for cheetah in cheetahs:
            result += f'{cheetah}\n'

        return result[:-1]

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        keepers = [obj for obj in self.workers if obj.__class__.__name__ == "Keeper"]
        caretakers = [obj for obj in self.workers if obj.__class__.__name__ == "Caretaker"]
        vets = [obj for obj in self.workers if obj.__class__.__name__ == "Vet"]

        result += f'----- {len(keepers)} Keepers:\n'
        for keeper in keepers:
            result += f'{keeper}\n'

        result += f'----- {len(caretakers)} Caretakers:\n'
        for caretaker in caretakers:
            result += f'{caretaker}\n'

        result += f'----- {len(vets)} Vets:\n'
        for vet in vets:
            result += f'{vet}\n'

        return result[:-1]
