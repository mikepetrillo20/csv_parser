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

# loads csv file data into two array data structures
class LoadArray:
    def __init__(self, csv_file):
        self.rows = []
        self.titles = []
        self.csv_file = csv_file

    def __len__(self):
        return len(self.rows)
    
    def read(self):
        print(" ".join(self.titles))
        for row in self.rows:
            print(" ".join(row))

    def set_rows(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                self.rows.append(row)

    def set_title_bar(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.titles = next(csvreader)

    def get_title_bar(self):
        d = {}
        for index, title in enumerate(self.titles):
            d[index] = title
        return d

    def sort_array(self, column):
        # TODO: test other solutions here
        # TODO: every item is a string, wont sort int column yet
        self.rows.sort(key = lambda x: x[column])

if __name__ == "__main__":
    user_csv_file = ''
    choice = ''
    
    # loop to get the csv file and load it
    while True:
        user_csv_file = input('Please enter the exact name of your csv file: ')
        try:
            user = LoadArray(user_csv_file)
            user.set_title_bar()
            user.set_rows()
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
            # TODO: add a way for user to select what row that want to sort by
            user.sort_array(1)
            t1 = time.time()
            print(f'Finished Sorting in {t1-t0} seconds.')
        elif choice == '3':
            print('Feature will be implemented soon.')
        elif choice == '4':
            print('Feature will be implemented soon.')
        elif choice == '5':
            print('Feature will be implemented soon.')
