import unittest
from src.package_1 import module_2


class TestModule(unittest.TestCase):
    def test_function(self):
        result = module_2.function(3, 2)
        self.assertEquals(result,1)