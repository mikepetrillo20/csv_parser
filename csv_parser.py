import csv

def menu():
    print('Please select an option below:')
    print('1: Load')
    print('2: Print')
    print('3: TODO')
    print('4: TODO')
    print('5: TODO')
    print('q: Quit')


class ParserUsingArray:

    def __init__(self, csv_file):
        self.rows = []
        self.titles = []
        self.csv_file = csv_file
    
    # prints the title row then each following row according to a user input number
    def read(self, number_of_rows=9999):
        print(self.titles)
        for row in self.rows[:number_of_rows]:
            print(row)

    def get_rows(self):
        # reading the csv file
        with open(self.csv_file, 'r') as csvfile:
            # creating the csv reader object
            csvreader = csv.reader(csvfile)

            # skips first row
            next(csvreader)

            # grabbing each data row one by one
            for row in csvreader:
                self.rows.append(row)

    def get_titles(self):
        # reading the csv file
        with open(self.csv_file, 'r') as csvfile:
            # creating the csv reader object
            csvreader = csv.reader(csvfile)

            # grabbing the first row and moving pointer to following row
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
    
    # instantiating ParserUsingArray class with the user_file selection
    user = ParserUsingArray(user_file)

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
            user.read(int(input('How many rows would you like to read? ')))
        elif selection == '3':
            print('Feature will be implemented soon.')
        elif selection == '4':
            print('Feature will be implemented soon.')
        elif selection == '5':
            print('Feature will be implemented soon.')
