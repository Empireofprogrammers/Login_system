import PasswordGenerator
import unittest
class testPasswordGenerator(unittest.TestCase):
    def testManupulatingVaribles(self):
        passwordGenerator = PasswordGenerator.PasswordGenerator()
        passwordGenerator.__LowerCharacterList = None
        passwordGenerator.__LowerCharacterList = 47855
        return passwordGenerator.__LowerCharacterList

if __name__ == '__main__':
    TestObj = testPasswordGenerator()
    print(TestObj.testManupulatingVaribles())