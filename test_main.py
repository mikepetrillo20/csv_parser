import unittest
import main

class TestLoadArray(unittest.TestCase):
    
    def setUp(self):
        self.test = main.LoadArray('test_data.csv')
        self.test.set_rows()
        self.test.set_title_bar()

    def test_len(self):
        self.assertEqual(len(self.test), 10)
    
    def test_get_rows(self):
        self.assertEqual(self.test.rows[0][0], '1000002330')
        self.assertEqual(self.test.rows[9][0], '100004195')
        self.assertEqual(self.test.rows[0][1], 'The Songs of Adelaide & Abullah')
        self.assertEqual(self.test.rows[9][1], 'STUDIO IN THE SKY - A Documentary Feature Film (Canceled)')
    
    def test_get_titles(self):
        self.assertEqual(self.test.titles[0], 'ID')
        self.assertEqual(self.test.titles[1], 'name')
        self.assertEqual(self.test.titles[2], 'category')
        self.assertEqual(self.test.titles[3], 'main_category')

    def tearDown(self):
        self.test = None

if __name__ == "__main__":
    unittest.main()