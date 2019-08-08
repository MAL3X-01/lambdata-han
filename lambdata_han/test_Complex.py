import unittest
from Complex import Complex

class TestComplexMethods(unittest.TestCase):

    def test_add(self):
        complex1 = Complex(1, 2)
        complex2 = Complex(2, 3)
        complex_add_test = complex1.add(complex2)
        
        self.assertEqual(complex_add_test.r, 3)
        self.assertEqual(complex_add_test.i, 5)

    def test_sub(self):
        complex1 = Complex(1, 2)
        complex2 = Complex(2, 3)
        complex_sub_test = complex1.sub(complex2)
        
        self.assertEqual(complex_sub_test.r, -1)
        self.assertEqual(complex_sub_test.i, -1)
        
    def test_conj(self):
        complex1 = Complex(1, 2)
        
        self.assertEqual(complex1.conj().r, 1)
        self.assertEqual(complex1.conj().i, -2)
    
    def test_mul(self):
        complex1 = Complex(3, 2)
        complex2 = Complex(1, 7)
        complex_mul_test = complex1.mul(complex2)
        
        self.assertEqual(complex_mul_test.r, -11)
        self.assertEqual(complex_mul_test.i, 23)

    def test_div(self):
        complex1 = Complex(2, -1)
        complex2 = Complex(-3, 6)
        complex_div_test = complex1.div(complex2)

        
        self.assertEqual(complex_div_test.r, -4/15)
        self.assertEqual(complex_div_test.i, -1/5)
        

if __name__ == '__main__':
    unittest.main()