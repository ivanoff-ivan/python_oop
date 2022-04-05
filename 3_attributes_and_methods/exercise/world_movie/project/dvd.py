class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split(".")
        year = int(date[2])
        month = int(date[1])
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        rented_or_not = ""
        if self.is_rented:
            rented_or_not = "rented"
        else:
            rented_or_not = "not rented"

        return f"{self.id}: {self.name} " \
               f"({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {rented_or_not}"


from dvd import DVD

import unittest


class TestsMovieWorld(unittest.TestCase):
    def test_dvd_class_method(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(dvd.name, "A")
        self.assertEqual(dvd.id, 1)
        self.assertEqual(dvd.creation_month, "October")
        self.assertEqual(dvd.creation_year, 1997)
        self.assertEqual(dvd.age_restriction, 18)
        self.assertEqual(dvd.is_rented, False)


if __name__ == "__main__":
    unittest.main()
