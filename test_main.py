import unittest
import main

class TestData(unittest.TestCase):
    
    def setUp(self):
        self.test = main.Data('test_data.csv')
        self.test.build_array()

    def test_len(self):
        self.assertEqual(len(self.test), 10)
    
    def test_set_rows(self):
        self.assertEqual(self.test.rows[0][0], 1000002330)
        self.assertEqual(self.test.rows[9][0], 100004195)
        self.assertEqual(self.test.rows[0][1], 'The Songs of Adelaide & Abullah')
        self.assertEqual(self.test.rows[9][1], 'STUDIO IN THE SKY - A Documentary Feature Film (Canceled)')
    
    def test_set_title_bar(self):
        self.assertEqual(self.test.columns[0], 'ID')
        self.assertEqual(self.test.columns[1], 'name')
        self.assertEqual(self.test.columns[2], 'category')
        self.assertEqual(self.test.columns[3], 'main_category')

    def test_sort_array(self):
        self.test.sort_array(1)
        self.assertEqual(self.test.rows[0][1], 'Chaser Strips. Our Strips make Shots their B*tch!')
        self.assertEqual(self.test.rows[4][1], 'SPIN - Premium Retractable In-Ear Headphones with Mic')
        self.assertEqual(self.test.rows[9][1], 'Where is Hank?')

        self.test.sort_array(2)
        self.assertEqual(self.test.rows[0][2], 'Documentary')
        self.assertEqual(self.test.rows[4][2], 'Music')
        self.assertEqual(self.test.rows[9][2], 'Restaurants')

        # TODO: add additional tests to test int and double rows

    def tearDown(self):
        self.test = None

if __name__ == "__main__":
    unittest.main()