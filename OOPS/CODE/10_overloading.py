class Complex:
    def __init__(self, real, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    def __str__(self):
        return "(%g+%gj)" % (self.real, self.imag)

    # self + other
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # self - other
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

c = Complex(2,3)

print(c + 14.0)

print(c - 4.0)

print(str(c))