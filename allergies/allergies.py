class Allergies(object):

    allergies = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return bool(self.score & 1 << self.allergies.index(item))

    @property
    def lst(self):
        return [
            self.allergies[i]
            for i in range(len(self.allergies))
            if self.is_allergic_to(self.allergies[i])
        ]
