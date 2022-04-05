from converters.JsonConverter import JsonConverter
from converters.decorators.PrimitiveValuesDecoratorConverter import PrimitiveValuesDecoratorConverter
from converters.factories.CsvConverter import CsvConverter


class ConverterFactory:
    def __init__(self):
        self.converters = {
            "application/json": JsonConverter(),
            "application/vnd.ms-excel": PrimitiveValuesDecoratorConverter(CsvConverter()),
        }



    def get_converter(self, type):
        if type not in self.converters:
            raise ValueError(f"No converter for type {type}")

        return self.converters[type]
