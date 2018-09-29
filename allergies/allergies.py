class Allergies(object):

    allergies = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score
        self._lst = [
            allergie
            for allergie in self.allergies
            if self.is_allergic_to(allergie)
        ]

    def is_allergic_to(self, item):
        return bool(self.score & self.allergies[item])

    @property
    def lst(self):
        return self._lst
