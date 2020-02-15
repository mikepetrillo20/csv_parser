'''
TODO: build out functionality to choose delimiter
TODO: figure out how to convert dates and sort them properly
'''

import csv
from operator import itemgetter


def menu():
    print('1: Print')
    print('2: Sort')
    print('3: Overwrite File')
    print('4: Create New File')
    print('q: Quit')


class CSVParser:
    def __init__(self, csv_file):
        self.rows = []
        self.columns = []
        self.csv_file = csv_file

    def __len__(self):
        return len(self.rows)

    def read(self):
        print(self.columns)
        for row in self.rows:
            print(row)
        print()

    def build_array(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self._get_columns(csvreader)
            self._get_rows(csvreader)

    def display_columns(self):
        for integer, column in enumerate(self.columns):
            print(f'{integer}: {column}')

    def sort_array(self, column):
        self.rows.sort(key=lambda x: x[column])

    def overwrite_or_create_file(self, file_name):
        with open(file_name, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            # writes the column row first
            csvwriter.writerow(self.columns)
            # loops through rows
            for row in self.rows:
                csvwriter.writerow(row)

    def _get_rows(self, reader):
        # creates a list of rows, each row is a list
        for row in reader:
            row = self._convert_potential_number(row)
            self.rows.append(row)

    def _get_columns(self, reader):
        # grabs the first row in a .csv (usually title row)
        self.columns = next(reader)

    def _convert_potential_number(self, row):
        new_row = []
        for item in row:
            try:
                # try to convert str to int first
                new_row.append(int(item))
            except ValueError:
                try:
                    # try to convert str to float second
                    new_row.append(float(item))
                except ValueError:
                    new_row.append(item)
        return new_row


if __name__ == "__main__":
    user_csv_file = ''
    choice = ''  # user menu() choice

    # loop to assign the csv file, check validity, and load it
    while True:
        user_csv_file = input('Please enter the exact name of your csv file: ')
        try:
            user = CSVParser(user_csv_file)
            user.build_array()
            print(f'This csv file has {len(user)} rows.')
            break
        except FileNotFoundError:
            print('Please enter a valid .csv file.')

    # main loop for menu() interaction
    while choice is not 'q':
        menu()
        choice = input('What would you like to do? ')
        print()

        if choice == '1':  # print
            user.read()
        elif choice == '2':  # sort
            user.display_columns()
            column_choice = input('Which row to sort by? ')
            print()

            # loop to assign and check valid column choice
            while True:
                try:
                    user.sort_array(int(column_choice))
                    break
                except IndexError:
                    column_choice = input('Please choose a valid option. ')
                    print()
        elif choice == '3':  # Overwrite File
            user.overwrite_or_create_file(user.csv_file)
            print('File overwritten.\n')
        elif choice == '4':  # Create New File
            new_file_name = input('New file name (example.csv): ')
            # loop to check for valid file name
            while new_file_name[-4:] != '.csv':
                new_file_name = input('Please end your file name with .csv: ')
            user.overwrite_or_create_file(new_file_name)
            print(f'\nCreated a new file named {new_file_name}.\n')
