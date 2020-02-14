import csv
import time
from operator import itemgetter


def menu():
    print('Please select an option below:')
    print('1: Print')
    print('2: Sort')
    print('3: TODO')
    print('4: TODO')
    print('5: TODO')
    print('q: Quit')


class Data:
    def __init__(self, csv_file):
        self.rows = []
        self.titles = []
        self.csv_file = csv_file

    def __len__(self):
        return len(self.rows)

    def read(self):
        # TODO: convert this to a dunder method
        print(self.titles)
        for row in self.rows:
            print(row)

    def build_array(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self._title_bar(csvreader)
            self._rows(csvreader)

    def get_title_bar(self):
        # TODO: figure out a better way to do this
        d = {}
        for index, title in enumerate(self.titles):
            d[index] = title
        return d

    def sort_array(self, column):
        self.rows.sort(key=lambda x: x[column])

    def _rows(self, reader):
        for row in reader:
            row = self._convert_potential_number(row)
            self.rows.append(row)

    def _title_bar(self, reader):
        self.titles = next(reader)

    def _convert_potential_number(self, row):
        new_row = []
        for item in row:
            try:
                new_row.append(int(item))
            except ValueError:
                try:
                    new_row.append(float(item))
                except ValueError:
                    new_row.append(item)
        return new_row


if __name__ == "__main__":
    user_csv_file = ''
    choice = ''

    # loop to get the csv file and load it
    while True:
        user_csv_file = input('Please enter the exact name of your csv file: ')
        try:
            user = Data(user_csv_file)
            user.build_array()
            print(f'This csv file has {len(user)} rows.')
            break
        except FileNotFoundError:
            print('Please enter a valid .csv file.')

    # main loop for user interaction
    while choice is not 'q':
        menu()
        choice = input('Please choose an option above: ')

        if choice == '1':
            user.read()
        elif choice == '2':
            t0 = time.time()
            # TODO: add a way for user to select what row they want to sort by
            user.sort_array(0)
            t1 = time.time()
            #TODO: find a more accurate time tracker
            print(f'Finished Sorting in {t1-t0} seconds.')
        elif choice == '3':
            print('Feature will be implemented soon.')
        elif choice == '4':
            print('Feature will be implemented soon.')
        elif choice == '5':
            print('Feature will be implemented soon.')
