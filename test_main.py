import unittest
import main

class TestData(unittest.TestCase):
    
    def setUp(self):
        self.test = main.CSVParser('test_data.csv')
        self.test.build_array()

    def test_len(self):
        self.assertEqual(len(self.test), 10)
    
    def test_get_rows(self):
        self.assertEqual(self.test.rows[0][0], 1000002330)
        self.assertEqual(self.test.rows[9][0], 100004195)
        self.assertEqual(self.test.rows[0][1], 'The Songs of Adelaide & Abullah')
        self.assertEqual(self.test.rows[9][1], 'STUDIO IN THE SKY - A Documentary Feature Film (Canceled)')
    
    def test_get_columns(self):
        self.assertEqual(self.test.columns[0], 'ID')
        self.assertEqual(self.test.columns[1], 'name')
        self.assertEqual(self.test.columns[2], 'category')
        self.assertEqual(self.test.columns[3], 'main_category')

    def test_sort_array(self):
        # sort by int
        self.test.sort_array(0)
        self.assertEqual(self.test.rows[0][0], 100004195)
        self.assertEqual(self.test.rows[4][0], 1000007540)
        self.assertEqual(self.test.rows[9][0], 1000034518)

        # sort by string
        self.test.sort_array(1)
        self.assertEqual(self.test.rows[0][1], 'Chaser Strips. Our Strips make Shots their B*tch!')
        self.assertEqual(self.test.rows[4][1], 'SPIN - Premium Retractable In-Ear Headphones with Mic')
        self.assertEqual(self.test.rows[9][1], 'Where is Hank?')

        # sort by float
        self.test.sort_array(6)
        self.assertEqual(self.test.rows[0][6], 1000.0)
        self.assertEqual(self.test.rows[4][6], 25000.0)
        self.assertEqual(self.test.rows[9][6], 125000.0)


    def tearDown(self):
        self.test = None

if __name__ == "__main__":
    unittest.main()