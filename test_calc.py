
import unittest
import calc

class testcalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(2,16),18)
        self.assertEqual(calc.addition(10,1),11)
        self.assertEqual(calc.addition(11,2),13)

        self.assertEqual(calc.addition(10.5,3),30.5)
        self.assertEqual(calc.addition(10,16),25)

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(20,16),4)
        self.assertEqual(calc.subtraction(2,1),1)
        self.assertEqual(calc.subtraction(11,1),10)

        self.assertEqual(calc.subtraction(10.5,3),30.5)
        self.assertEqual(calc.subtraction(10,16),-6)
    def test_multiplication(self):
        self.assertEqual(calc.multiplication(2,3),6)
    def test_division(self):
        self.assertEqual(calc.division(6,2),3)

if __name__=="main":
    unittest.main()
