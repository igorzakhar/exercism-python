class SpaceAge(object):

    ORBITAL_PERIOD = [(k, v * 31557600) for k, v in (
        ('earth', 1.0),
        ('mercury', 0.2408467),
        ('venus', 0.61519726),
        ('mars', 1.8808158),
        ('jupiter', 11.862615),
        ('saturn', 29.447498),
        ('uranus', 84.016846),
        ('neptune', 164.79132)
    )]

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, period in self.ORBITAL_PERIOD:
            self._add_method(planet, period)

    def _add_method(self, planet, period):
        def space_age_calc():
            return round(self.seconds / period, 2)
        setattr(self, 'on_' + planet, space_age_calc)
