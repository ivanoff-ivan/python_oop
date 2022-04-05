class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __str__(self):
        people_str = ', '.join([str(person) for person in self.people])
        return "Group " + self.name + " with members " + people_str

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return "Person " + str(index) + ": " + str(self.people[index])

    def __add__(self, other):
        return Group(self.name, self.people + other.people)

import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("One", "First")
        self.person_2 = Person("Two", "Second")
        self.person_3 = Person("Three", "Third")
        self.person_4 = Person("Four", "Fourth")

        self.group_1 = Group("First Group", [self.person_1, self.person_2])

    def test_person_init_method(self):
        self.assertEqual(self.person_1.name, "One")
        self.assertEqual(self.person_1.surname, "First")

    def test_person_add_method(self):
        new_person = self.person_1 + self.person_2
        self.assertEqual(new_person.name, "One")
        self.assertEqual(new_person.surname, "Second")

    def test_person_str_method(self):
        result = str(self.person_4)
        expected_result = "Four Fourth"
        self.assertEqual(result, expected_result)

    def test_group_init_method(self):
        self.assertEqual(self.group_1.name, "First Group")
        expected_list = [self.person_1, self.person_2]
        self.assertListEqual(self.group_1.people, expected_list)

    def test_group_len_method(self):
        result = len(self.group_1)
        self.assertEqual(result, 2)

    def test_group_getitem_method(self):
        result = str(self.group_1[1])
        expected_result = f"Person 1: Two Second"
        self.assertEqual(expected_result, result)

    def test_group_add_method(self):
        group_2 = Group("Second Group", [self.person_3])
        group_3 = self.group_1 + group_2
        self.assertEqual(self.group_1.name, group_3.name)
        self.assertEqual(len(group_3.people), 3)

    def test_group_str_method(self):
        result = str(self.group_1)
        expected_result = "Group First Group with members One First, Two Second"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
