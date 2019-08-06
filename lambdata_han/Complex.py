

class Complex:

    def __init__(self, realpart, imagpart):        
        self.r = realpart
        self.i = imagpart
        
    def __repr__(self):
        return "{0:}{1:+}i".format(self.r, self.i)#f'({self.r}{self.i}i)'
        
    def add(self, complex):
        return Complex(self.r + complex.r, self.i + complex.i)
        
    def sub(self, complex):
        return Complex(self.r - complex.r, self.i - complex.i)
    
    def mul(self, complex):
        return Complex(self.r * complex.r - self.i * complex.i,
                       self.r * complex.i + self.i * complex.r)
                       
    def conj(self):
        return Complex(self.r, -self.i)
                       
    def div(self, complex):
        top = self.mul(complex.conj())
        bottom = complex.mul(complex.conj())
        return Complex(top.r/bottom.r, top.i/bottom.r)