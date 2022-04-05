from converters.factories.Converter import Converter


def can_convert_float(value):
    try:
        float(value)
        return True
    except:
        return False


def convert_to_float(value):
    return float(value)


def can_convert_int(value):
    try:
        int(value)
        return True
    except:
        return False


def convert_to_int(value):
    return int(value)


def can_convert_bool(value):
    return value in ['true', 'false', 'True', 'False']


def convert_to_bool(value):
    return value in ['true', 'True']


class PrimitiveValuesDecoratorConverter(Converter):
    def __init__(self, converter: Converter):
        self.converter = converter

    def convert_from_stream(self, stream):
        result = self.converter.convert_from_stream(stream)
        for key, value in result.items():
            if can_convert_int(value):
                result[key] = convert_to_int(value)
            elif can_convert_float(value):
                result[key] = convert_to_float(value)
            elif can_convert_bool(value):
                result[key] = convert_to_bool(value)

            return result
