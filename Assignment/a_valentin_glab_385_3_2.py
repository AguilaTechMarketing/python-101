# Alejandro Valentin
# GLAB 385.3.2
# July 2026

import csv
import os

file_path = 'country.csv'

# 0. SETUP: Ensure the data file exists for the instructor
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding="utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'area', 'country_code2', 'country_code3'])
        writer.writerow(['United States', '9833520', 'US', 'USA'])
        writer.writerow(['Canada', '9984670', 'CA', 'CAN'])
        writer.writerow(['Mexico', '1972550', 'MX', 'MEX'])

# 1. Technique: Enumerate (Identifying Header vs Data)
def run_task_enumerate():
    print("\n====================================")
    print("\n--- Task: Using Enumerate to ID Header ---\n")
    print("====================================\n")
    with open(file_path, encoding="utf8") as f:
        reader = csv.reader(f)
        for line_no, line in enumerate(reader, 1):
            if line_no == 1:
                print(f"Header: {line}")
            else:
                print(f"Data Row {line_no}: {line}")

# 2. Technique: Using next() to skip header
def run_task_next():
    print("\n====================================")
    print("\n--- Task: Using next() to skip header ---\n")
    print("====================================\n")
    with open(file_path, encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader) # Skips the first row
        for line in reader:
            print(line)

# 3. Technique: DictReader
def run_task_dict_reader():
    print("\n====================================")
    print("\n--- Task: DictReader ---\n")
    print("====================================\n")
    with open(file_path, encoding="utf8") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"The area of {line['name']} is {line['area']} km2")

# 4. Technique: Custom Fieldnames
def run_task_custom_fields():
    print("\n====================================")
    print("\n--- Task: Custom Fieldnames ---\n")
    print("====================================\n")
    fieldnames = ['country_name', 'area', 'code2', 'code3']
    with open(file_path, encoding="utf8") as f:
        reader = csv.DictReader(f, fieldnames=fieldnames)
        next(reader) # Skip the original header to avoid it being read as data
        for line in reader:
            print(f"The area of {line['country_name']} is {line['area']} km2")

if __name__ == "__main__":
    run_task_enumerate()
    run_task_next()
    run_task_dict_reader()
    run_task_custom_fields()