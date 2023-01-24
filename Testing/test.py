import unittest
from jump import jump

# Implement a test inside the given function that shows a flaw in the function "jump"
# the test should pass when the "jump" function works accordingly.


class TestJumpFunction(unittest.TestCase):

    def testJump(self):
        self.assertEqual(jump(228), "The jumper qualifies for the final.")
   

if __name__ == '__main__':
    unittest.main()
