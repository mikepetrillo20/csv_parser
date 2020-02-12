import csv

class ListParser:

    def __init__(self):
        self.rows = []
        self.titles = []

    def parse_to_list(self, csv_file):
        # reading the csv file
        with open(csv_file, 'r') as csvfile:
            # creating the csv reader object
            csvreader = csv.reader(csvfile)

            # grabbing the first row and moving pointer to following row
            self.titles = next(csvreader)

            # grabbing each data row one by one
            for row in csvreader:
                self.rows.append(row)


test = ListParser()
test.parse_to_list('small_data.csv')
print(test.rows)