import unittest
from arithmetic import add, subtract, multiply, divide

class TestArithmetic(unittest.TestCase):
    def test_add_positive_numbers(self):
        val = add(4,3)
        self.assertEqual(7, val)

    def test_add_negative_numbers(self):
        val = add(-4,-3)
        self.assertEqual(-7, val)

    def test_subtract_positive_numbers(self):
        val = subtract(4,3)
        self.assertEqual(1 , val)

    def test_subtract_negative_numbers(self):
        val = subtract(-4,-3)
        self.assertEqual(-1, val)
    def test_multiply(self):
        self.assertEqual(12, multiply(4, 3))

    def test_divide(self):
        self.assertEqual('1.667', divide(5, 3))

    def test_divide_by_zero(self):
        with self.assertRaises(Exception) as context:
            divide(5, 0)
        self.assertTrue('Divide by zero!', context.exception)

#if __name__ == "__main__":
#    unittest.main()
