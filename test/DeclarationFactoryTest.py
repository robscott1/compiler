import unittest
from src.DeclarationFactory import DeclarationFactory as df
from natives.IntType import IntType

class DeclarationFactoryTest(unittest.TestCase):

    def test_type_switch(self):
        self.assertEqual(df.type_switch(self, type="int").__class__, IntType)

if __name__ == '__main__':
    unittest.main()