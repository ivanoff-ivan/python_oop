from abc import ABC, abstractmethod


class DataConverterAbstractFactory(ABC):
    @abstractmethod
    def get_json_converter(self):
        pass

    @abstractmethod
    def get_csv_converter(self):
        pass


"""
the rest of the implementation is the same
"""
