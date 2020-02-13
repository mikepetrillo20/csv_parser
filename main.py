import csv

def menu():
    print('Please select an option below:')
    print('1: Load')
    print('2: Print')
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
    
    def read(self, num_rows=10):
        print(self.titles)
        for row in self.rows[:num_rows]:
            print(row)

    def get_rows(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                self.rows.append(row)

    def get_titles(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.titles = next(csvreader)

if __name__ == "__main__":
    # user choice selection
    selection = ''
    # user csv file
    user_file = ''
    # user error checking conditional
    happy = 'n'

    # loop to grab the csv file the user wants to work with
    while happy is not 'y':
        user_file = input('Please enter the exact name of your csv file: ')
        happy = input(f'You chose: {user_file}, is this correct? y or n: ')
    
    # instantiate LoadArray class with the user_file selection
    user = LoadArray(user_file)

    # loop to allow the user to use the methods and functions above
    while selection is not 'q':
        # print out the feature menu
        menu()
        selection = input('Please choose an option above: ')

        # user choices and logic
        if selection == '1':
            user.get_titles()
            user.get_rows()
        elif selection == '2':
            print(f'This csv file has {len(user)} rows.')
            user.read(int(input('How many rows would you like to read? ')))
        elif selection == '3':
            print('Feature will be implemented soon.')
        elif selection == '4':
            print('Feature will be implemented soon.')
        elif selection == '5':
            print('Feature will be implemented soon.')
