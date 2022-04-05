class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return self.name + " " + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([f'{p.name} {p.surname}' for p in self.people])}"

    def __getitem__(self, item):
        return f"Person {item}: " + self.people[item].name + " " + self.people[item].surname

    def __add__(self, other):
        new_peeps_list = [p for p in self.people]
        new_peeps_list.extend(other.people)
        return Group(self.name, new_peeps_list)


import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')

    def test_person_str(self):
        self.assertEqual(str(self.p1), 'Bill Gates')


if __name__ == "__main__":
    unittest.main()