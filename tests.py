import unittest
from Calc import Calculator 

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(7, 8), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(4, 8), 4)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 10), 20)
        self.assertEqual(self.calc.multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
