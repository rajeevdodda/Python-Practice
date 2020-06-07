# Example 8-14. Passengers disappear when dropped by a TwilightBus


class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']

bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')

print(basketball_team)