import unittest
from package_1 import module


class TestModule(unittest.TestCase):
    def test_function(self):
        result = module.function(1,2)
        self.assertEquals(result,3)