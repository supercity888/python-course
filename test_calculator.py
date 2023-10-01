import calculator
import unittest

class testCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(7, -90), -83)
        self.assertEqual(calculator.add(-1, -55), -56)

    def test_substraction(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(8, -1), 9)
        self.assertEqual(calculator.sub(-7, -3), -4)
        self.assertEqual(calculator.sub(-4, 2), -6)

    def test_multi(self):
        self.assertEqual(calculator.multi(2, 3), 6)
        self.assertEqual(calculator.multi(-5, 2), -10)
        self.assertEqual(calculator.multi(-3, -3), 9)

    def test_div(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertEqual(calculator.div(-9, -3), 3)
        self.assertEqual(calculator.div(4, -1), -4)



if __name__ == "__main__":
    unittest.main()