def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DataImporter:
    def __init__(self):
        pass


d1 = DataImporter()
d2 = DataImporter()
print(d1 == d2)
