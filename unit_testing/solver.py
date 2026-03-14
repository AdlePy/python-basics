class Solver:
    EXCEPTION_TEXT_INVALID_TYPE = "a and b should be numbers"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mult(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float))):
            raise TypeError(self.EXCEPTION_TEXT_INVALID_TYPE)

        return self.a * self.b
