import csv
from operator import itemgetter


def menu():
    print('1: Print')
    print('2: Sort')
    print('3: Overwrite File')
    print('4: Create New File')
    print('q: Quit')


class Data:
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

    def overwrite_file(self):
        with open(self.csv_file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            # overwrites the column row first
            csvwriter.writerow(self.columns)
            # loops through rows and overwrites them
            for row in self.rows:
                csvwriter.writerow(row)
                
    def create_new_file(self, new_file_name):
        pass

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
            user = Data(user_csv_file)
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
            user.overwrite_file()
            print('File overwritten.')
        elif choice == '4':  # Create New File
            pass # TODO: add functionality
