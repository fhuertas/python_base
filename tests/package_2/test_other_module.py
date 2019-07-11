import unittest

from src.package_2 import other_module


class TestModule(unittest.TestCase):
    def test_function(self):
        result = other_module.function_2(1, 2)
        self.assertEquals(result,3)
