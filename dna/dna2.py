import csv

file_name = "databases/small.csv"

# Open the csv file
with open(file_name, "r") as database:
    # Create a dictionary with fieldnames as keys and data as values
    csv_reader = csv.DictReader(database)

    # Print out each person's names
    for line in csv_reader:
        print(line['name'])

    # with open('databases/new_database', 'w') as new_data:
    #     csv_writer = csv.writer(new_data)

    #     for line in csv_reader:
    #         csv_writer.writerow(line)


    # # Skip the first line
    # next(csv_reader)

    # # Print the names of people with more than 2 repeats of 'AGATC'
    # for line in csv_reader:
    #     if int(line[1]) > 2:
    #         print(line[0])

