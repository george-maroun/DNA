import csv
import sys

def main():

    with open(sys.argc[1]) as database:
        csv_reader = csv.DictReader(database)

        STRs = csv_reader[:1]

        dict = 