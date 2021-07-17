"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        "set two variables, a start variable that the user can set manually, and a hidden counter variable."
        self.start = start
        self.counter = -1
    
    def generate(self):
        "add one to the counter and return the sum of the start and counter"
        self.counter += 1
        return self.start + self.counter

    def reset(self):
        "set the counter to 0"
        self.counter = -1

