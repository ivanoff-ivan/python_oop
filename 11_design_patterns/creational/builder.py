from utils.print_attrs import IPrintAttributes


class Animal(IPrintAttributes):
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight


class AnimalsBuilder():
    mandatory_attributes = {"name": str, "age": int, "species": str}
    optional_attributes = {"weight": float}

    def __init__(self):
        self.__attrs_dict = {}
        self.__reset()

    def set_name(self, name):
        self.__attrs_dict["name"] = name
        return self

    def set_age(self, age):
        self.__attrs_dict["age"] = age
        return self

    def set_species(self, species):
        self.__attrs_dict["species"] = species
        return self

    def set_weight(self, weight):
        self.__attrs_dict["weight"] = weight
        return self

    def __reset(self):
        for key, pair in self.mandatory_attributes.items():
            self.__attrs_dict[key] = None

        for key, pair in self.optional_attributes.items():
            self.__attrs_dict[key] = None

    def __validate(self):
        missing_values = [key for key in self.mandatory_attributes.keys() if self.__attrs_dict[key] is None]
        if missing_values:
            raise ValueError(f"The following attributes are missing: {''.join(missing_values)}")

    def build(self):
        self.__validate()
        result = Animal(**self.__attrs_dict)
        self.__reset()
        return result


print(Animal("Gosho", 3, "Kuche", 123))  # tova e bez builder...

builder = AnimalsBuilder()
builder.set_name("Pesho")
builder.set_age(4)
builder.set_species("cat")  # ako ne podadem species shte grumne
builder.set_weight(2)  # ako ne podadem weight, nqma da ima problem, zashtoto sme go napravili optional
print(builder.build())

print(builder
      .set_name("Pesho")
      .set_age(4)
      .set_species("cat")
      .set_weight(2)
      .build()
      )
