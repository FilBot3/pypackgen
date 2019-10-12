""" pypackgen_test.py
"""

import unittest


class TestPyPackGen(unittest.TestCase):
    """ TestPyPackGen Test Case
    """

    def test_phil(self):
        """ TestPhil adds numbers
        """
        self.assertEqual(3 + 2, 5)


if __name__ == '__main__':
    unittest.main()
