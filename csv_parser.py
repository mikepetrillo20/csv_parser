import csv

class ParserUsingArray:

    def __init__(self):
        self.rows = []
        self.titles = []
    
    # prints the title row then each following row according to a user input number
    def read(self, number_of_rows=9999):
        print(self.titles)
        for row in self.rows[:number_of_rows]:
            print(row)

    # parses the csv file feeding the data received into two arrays
    def parse_to_array(self, csv_file):
        # reading the csv file
        with open(csv_file, 'r') as csvfile:
            # creating the csv reader object
            csvreader = csv.reader(csvfile)

            # grabbing the first row and moving pointer to following row
            self.titles = next(csvreader)

            # grabbing each data row one by one
            for row in csvreader:
                self.rows.append(row)
    
# TESTING for ParserUsingArray
test = ParserUsingArray()
test.parse_to_array('small_data.csv')
test.read(10)

