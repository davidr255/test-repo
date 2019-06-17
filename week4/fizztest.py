from unittest import TestCase
from fizzbuzz import Fizzbuzzer

class TestFuzz(TestCase):

    def testZerocase(self):
        x = Fizzbuzzer()
        first_outcome = x.number
        self.assertEqual(first_outcome, 0, "first outcome is 0.")
    
    def testNext(self):
        x = Fizzbuzzer()
        next_outcome = x.next()
        self.assertIsInstance(next_outcome, str, "next ouctome is a string.")
        self.assertEqual(next_outcome, "1", "next outcome is 1.")
    
    def testFizz(self):
        x = Fizzbuzzer(2)
        next_outcome = x.next()
        self.assertEqual(next_outcome, "fizz")
        next_outcome = x.next()
        self.assertEqual(next_outcome, "4")
