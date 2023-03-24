class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return self.instrument


class Band(Musician):
    instances = []

    def __init__(self, name, members):
        # Musician.__init__(self, name)
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f'This band is {self.name} and it consists of {self.members}'

    def __repr__(self):
        return f'{__class__.__name__} instance. Name = {self.name}, Band Members = {self.members}'

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())

        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist(Musician):
    instrument = 'guitar'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    instrument = 'bass'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    instrument = 'drums'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


if __name__ == '__main__':
    joan = Guitarist('Joan Jett')
    members = [
        Guitarist("Kurt Cobain"),
        Bassist("Krist Novoselic"),
        Drummer("Dave Grohl"),
    ]
    nirvana_band = Band("Nirvana", members)

    print(nirvana_band.play_solos())

    nirvana_band.__repr__()

    print(nirvana_band.to_list())
