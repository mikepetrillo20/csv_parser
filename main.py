import csv
from operator import itemgetter


def menu():
    print('1: Print')
    print('2: Sort')
    print('3: TODO')
    print('4: TODO')
    print('5: TODO')
    print('q: Quit')


class Data:
    def __init__(self, csv_file):
        self.rows = []
        self.columns = []
        self.csv_file = csv_file

    def __len__(self):
        return len(self.rows)

    def read(self):
        # TODO: convert this to a dunder method
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

    def display_rows(self):
        # TODO: find a way to display human readable rows
        pass

    def sort_array(self, column):
        self.rows.sort(key=lambda x: x[column])

    def _get_rows(self, reader):
        for row in reader:
            row = self._convert_potential_number(row)
            self.rows.append(row)

    def _get_columns(self, reader):
        self.columns = next(reader)

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
        choice = input('What would you like to do? ')
        print()

        if choice == '1':
            user.read()
        elif choice == '2':
            user.display_columns()
            column_choice = input('Which row to sort by? ')
            print()
            user.sort_array(int(column_choice))
        elif choice == '3':
            print('Feature will be implemented soon.')
        elif choice == '4':
            print('Feature will be implemented soon.')
        elif choice == '5':
            print('Feature will be implemented soon.')
