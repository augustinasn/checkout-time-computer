import unittest
from checkout_time_computer import CheckoutTimeComputer


class TestCheckoutTimeComputer(unittest.TestCase):
    def test_case_1(self):
        checkout_computer = CheckoutTimeComputer([5, 3, 4], 1)
        self.assertEqual(checkout_computer.compute_checkout_time(), 12)

    def test_case_2(self):
        checkout_computer = CheckoutTimeComputer([10, 2, 3, 3], 2)
        self.assertEqual(checkout_computer.compute_checkout_time(), 10)

    def test_case_3(self):
        checkout_computer = CheckoutTimeComputer([2, 3, 10], 2)
        self.assertEqual(checkout_computer.compute_checkout_time(), 12)