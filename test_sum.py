import unittest

from sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_int_negatives(self):
        data = [-1, -2, -3]
        result = sum(data)
        self.assertEqual(result, -6)
        
    def test_list_int_zero(self):
        data = [-1, -2, 3]
        result = sum(data)
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()