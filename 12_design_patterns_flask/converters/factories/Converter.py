from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def convert_from_stream(self, stream):
        pass
