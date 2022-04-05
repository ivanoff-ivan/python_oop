class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [obj for obj in self.supplies if obj.__class__.__name__ == "FoodSupply"]
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [obj for obj in self.supplies if obj.__class__.__name__ == "WaterSupply"]
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_medicines = [obj for obj in self.medicine if obj.__class__.__name__ == "Painkiller"]
        if len(painkillers_medicines) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_medicines

    @property
    def salves(self):
        salves_medicines = [obj for obj in self.medicine if obj.__class__.__name__ == "Salve"]
        if len(salves_medicines) == 0:
            raise IndexError("There are no salves left!")
        return salves_medicines

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            pills = [pill for pill in self.medicine if pill.__class__.__name__.lower() == medicine_type.lower()]
            if len(pills) > 0:
                pill = pills.pop()
                self.medicine.remove(pill)
                pill.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        return

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            substances = [supply for supply in self.supplies if
                          supply.__class__.__name__.lower() == sustenance_type.lower()]
            if len(substances) > 0:
                substance = substances.pop()
                self.supplies.remove(substance)
                substance.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
