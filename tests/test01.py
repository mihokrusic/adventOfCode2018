#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day01
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        result = day01.solve('+1, -2, +3, +1', 1)
        self.assertEqual(result, 3)
    def test_in(self):
        result = day01.solve(inputs.read_str("input01_actual"), 1)
        self.assertEqual(result, 454)

class Part2(unittest.TestCase):
    def test_01(self):
        result = day01.solve('+1, -1', 2)
        self.assertEqual(result, 0)
    def test_02(self):
        result = day01.solve('+7, +7, -2, -7, -4', 2)
        self.assertEqual(result, 14)
    def test_in(self):
        result = day01.solve(inputs.read_str("input01_actual"), 2)
        self.assertEqual(result, 566)

if __name__ == '__main__':
    unittest.main(verbosity=2)