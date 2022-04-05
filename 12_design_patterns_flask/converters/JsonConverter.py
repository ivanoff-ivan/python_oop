from json import loads

from converters.factories.Converter import Converter
from file_utils import read_all


class JsonConverter(Converter):
    def convert_from_stream(self, stream):
        return loads(read_all(stream))
