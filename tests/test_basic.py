from .context import gameoflife

import unittest

class BasicGridTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_basic_grid(self):
        grid = gameoflife.Grid()
        assert(grid.get_one() == 1)

if __name__ == '__main__':
    unittest.main()
