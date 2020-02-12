import csv
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0
    with open('small_data.csv', 'w', newline='') as small_csvfile:
        spamwriter = csv.writer(small_csvfile, delimiter=',')
        for row in spamreader:
            if count <= 9999:
                spamwriter.writerow(row)
                count += 1