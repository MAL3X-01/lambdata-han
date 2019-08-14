
class Complex:
    '''
    Class object to represent complex numbers
    
    Parameters:
        realpart: real part of the complex number
        imagpart: imaginary part of the complex number
    '''

    def __init__(self, realpart, imagpart):
        '''Creating complex numbers '''
        self.r = realpart
        self.i = imagpart
        
    def __repr__(self):
        '''  Print a string representation of object'''
        return "{0:}{1:+}i".format(self.r, self.i)#f'({self.r}{self.i}i)'
        
    def add(self, complex):
        '''Adding complex numbers '''
        return Complex(self.r + complex.r, self.i + complex.i)
        
    def sub(self, complex):
        '''Subtracting complex numbers '''
        return Complex(self.r - complex.r, self.i - complex.i)
    
    def mul(self, complex):
        '''Multiply complex numbers '''
        return Complex(self.r * complex.r - self.i * complex.i,
                       self.r * complex.i + self.i * complex.r)
                       
    def conj(self):
        ''' Conjucate a complex number'''
        return Complex(self.r, -self.i)
                       
    def div(self, complex):
        '''Divide complex number'''
        top = self.mul(complex.conj())
        bottom = complex.mul(complex.conj())
        return Complex(top.r/bottom.r, top.i/bottom.r)
    
