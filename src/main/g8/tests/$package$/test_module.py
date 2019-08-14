import unittest
from $package$ import module


class TestModule(unittest.TestCase):
    def test_function(self):
        result = module.function(1, 2)
        self.assertEquals(result,3)
