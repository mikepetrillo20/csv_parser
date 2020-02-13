import unittest
from csv_parser import ParserUsingArray

class TestParserUsingArray(unittest.TestCase):
    
    def setUp(self):
        self.test = ParserUsingArray('test_data.csv')
        self.test.get_rows()
        self.test.get_titles()

    def test_len(self):
        self.assertEqual(len(self.test), 10)

    def tearDown(self):
        self.test = None

if __name__ == "__main__":
    unittest.main()