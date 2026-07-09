# Alejandro Valentin
# GLAB 385.3.2
# July 2026

import csv

# csv.reader
def task_1_basic_reader(filename):
    print("\n====================================")
    print("\n--- Task 1: Basic CSV Reader ---\n")
    print("====================================\n")
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader) # Skip Header
        for row in reader:
            print(row)


# csv.DictReader
def task_2_dict_reader(filename):
    print("\n====================================")
    print("\n--- Task 2: DictReader ---\n")
    print("====================================\n")
    with open(filename, encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Country: {row['name']}, code: {row['country_code2']}")

# Main execution block
if __name__ == "__main__":
    file_path = 'country.csv'
    task_1_basic_reader(file_path)
    task_2_dict_reader(file_path)
