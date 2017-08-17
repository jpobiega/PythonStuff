import csv

# Put the full path to your CSV/Excel file here
MY_FILE = "../data/nba_stats_16-17.csv"

def parse(raw_file, delimiter):
    """ Parses a raw CSV file to a JSON-line object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data
    parsed_data = []

    fields = csv_data.next()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file

    opened_file.close()

    return parsed_data

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    # Let's see what the data looks like!
    print(new_data)

if __name__ == "__main__":
    main()
