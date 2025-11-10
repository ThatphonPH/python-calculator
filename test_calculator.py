##Thatphon Phetthong 6787033
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 10), 15)
    
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -10), -15)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_substract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
    
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide_even(self):
        self.assertEqual(self.calc.divide(20,4), 5)
    
    def test_divide_remainder(self):
        self.assertEqual(self.calc.divide(10, 3), 3)

    def test_modulo_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    
    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

if __name__ == '__main__':
    unittest.main()