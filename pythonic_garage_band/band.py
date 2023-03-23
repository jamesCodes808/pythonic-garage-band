class Band(Musician):
    def __init__(self, band_name,members):
        self.band_name = band_name
        self.members = members

    def __str__(self):
        return f'This band is {band.name} and it consists of {self.members}'

    def __repr__(self):
        return f''

    @classmethod
    def to_list(cls):
        return Band

class Musician():
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return self.instrument



class Guitarist(Musician):
    instrument = 'guitar'

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f'{self} instance. Name = {self.name}'

class Bassist(Musician):
    instrument = 'bass'

    def __init__(self, name):
        self.name = name


class Drummer(Musician):
    instrument = 'drums'
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    joan = Guitarist("Joan Jett")
