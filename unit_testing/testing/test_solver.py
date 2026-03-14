from unittest import TestCase
from solver import Solver


class SolverTestCase(TestCase):
    def setUp(self):
        self.s = Solver(2, 3)

    def test_add(self):
        result = self.s.add()
        self.assertEqual(result, 5)
        self.assertIsInstance(result, int)

    def test_mult(self):
        result = self.s.mult()
        self.assertEqual(result, 6)

    def test_mul_raises_type_error(self):
        s = Solver("", "0")

        with self.assertRaises(TypeError) as exc_info:
            s.mult()

        self.assertEqual(str(exc_info.exception), s.EXCEPTION_TEXT_INVALID_TYPE)
