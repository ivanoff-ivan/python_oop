import sys

from errors import CustomIndexError, CustomTypeError, CustomPopIndexError, CustomException


class CustomList:
    def __init__(self, *args):
        self.items = list(args)

    def index_is_valid(self, index):
        try:
            try_to_access = self.items[index]
            return True
        except IndexError as ex:
            raise CustomIndexError(f"CustomList does not have an element at this index "
                                   f"- {index}\nOriginal Exception was - {str(ex)}")
        except TypeError as ex:
            raise CustomTypeError(f"The index must be int. Your index is {type(index)} "
                                  f"\nOriginal Exception was - {str(ex)}")

    @staticmethod
    def get_value(item):
        value = 0
        numbers = [int, float]
        if type(item) in numbers:
            value += item
        elif isinstance(item, str):
            value += len(item)
        else:
            raise CustomException("The value is not valid!")
        return value

    def append(self, value):
        self.items = self.items + [value]
        return self.items

    def remove(self, index):
        if self.index_is_valid(index):
            value = self.items[index]
            del self.items[index]
            return value

    def get(self, index):
        if self.index_is_valid(index):
            value = self.items[index]
            return value

    def extend(self, *iterable):
        for el in iterable:
            self.append(el)
        return self.items

    def insert(self, index, value):
        if self.index_is_valid(index):
            self.items = self.items[:index] + [value] + self.items[index:]
            return self.items

    def pop(self):
        try:
            value = self.items[-1]
            del self.items[-1]
            return value
        except IndexError:
            raise CustomPopIndexError(f"Custom list has no elements in it!")

    def clear(self):
        self.items = []

    def index(self, value):
        for i in range(len(self.items)):
            if value == self.items[i]:
                return i
        return "Value not found!"

    def count(self, value):
        counter = 0
        for i in range(len(self.items)):
            if value == self.items[i]:
                counter += 1
        return counter

    def reverse(self):
        self.items = self.items[::-1]
        return self.items

    def copy(self):
        return self.items

    def size(self):
        return len(self.items)

    def add_first(self, value):
        self.items = [value] + self.items
        return self.items

    def dictionize(self):
        to_dict = {}
        for i in range(0, len(self.items), 2):
            try:
                to_dict[self.items[i]] = self.items[i + 1]
            except IndexError:
                to_dict[self.items[i]] = " "
        return to_dict

    def move(self, amount):
        if amount < 0:
            raise CustomException("Amount can not be negative number!")
        elif amount > len(self.items):
            raise CustomIndexError("The amount is invalid number!")
        try:
            self.items = self.items[amount:] + self.items[:amount]
            return self.items
        except IndexError:
            raise CustomIndexError(f"The amount of the items that you want to move"
                                   f" is greater than the total elements of the CustomList ")

    def sum(self):
        list_sum = 0
        for item in self.items:
            list_sum += self.get_value(item)
        return list_sum

    def overbound(self):
        index = 0
        biggest_value = float("-inf")
        for i in range(len(self.items)):
            value = self.get_value(self.items[i])
            if value > biggest_value:
                biggest_value = value
                index = i
        return index

    def underbound(self):
        index = 0
        smallest_value = float("inf")
        for i in range(len(self.items)):
            value = self.get_value(self.items[i])
            if value < smallest_value:
                smallest_value = value
                index = i
        return index
