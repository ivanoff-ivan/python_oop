class Cat:
    def sound(self):
        print("Meow!")


class Dog:
    def sound(self):
        print("Woof woof!")


def make_sound(animal_type):
    animal_type.sound()


cat = Cat()
dog = Dog()
make_sound(cat)
make_sound(dog)