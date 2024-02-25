# Ryan Wans 2024
import sys, csv, json
from pathlib import Path
from typing import Union

def transfer(input: Union[Path, str], output: Union[Path, str], preferred_names: Union[Path, str] = None):
    # create output file
    create_file(output)
    # read input file
    raw_grades = read_file(input)
    # read preferred names file
    if preferred_names:
        preferred_names = read_json_file(preferred_names)
    # write to output file
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Last Name', 'First Name', 'Student ID', 'Correct Points'])
        for row in raw_grades:
            # capture student data needed for Pearson
            student = {
                "firstName": row[0].split(" ")[0],
                "lastName": row[0].split(" ")[1],
                "sid": row[1],
                "points": row[4]
            }
            # check if student name should be replaced with actual name
            if preferred_names:
                capture = student["firstName"] + "#" + student["lastName"]
                if capture in preferred_names.keys():
                    student["firstName"] = preferred_names[capture].split("#")[0]
                    student["lastName"] = preferred_names[capture].split("#")[1]
                    print(f"Student's preferred name replaced: {student['firstName']} {student['lastName']}")
            # write to output file
            writer.writerow([student["lastName"], student["firstName"], student["sid"], student["points"]])
    print(f"Transfered grades of {len(raw_grades)} students.")

def create_file(file_path: Union[Path, str]):
    try:
        with open(file_path, 'x'):  # 'x' mode creates a new file; fails if the file already exists
            print(f"File created successfully at {file_path}")
    except FileExistsError:
        print(f"File already exists at {file_path}")
        sys.exit(1)

def read_file(file_path: Union[Path, str]) -> list[list[any]]:
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # skip first row
                if row[0] == "Name":
                    continue
                data.append(row)
        print(f"Importing grades of {len(data)} students.")
        return data
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        sys.exit(1)

def read_json_file(file_path: Union[Path, str]) -> dict[any]:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

if __name__ == "__main__":
    # get filename from command line argument
    # get optional third path for preffered names
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except IndexError:
        print("Usage: python transfer.py input_file.csv output_file.csv")
        sys.exit(1)
    try:
        preferred_names = sys.argv[3]
        print("Running with preferred names being replaced...")
    except IndexError:
        preferred_names = None

    if input_file == output_file:
        print("Input and output file cannot be the same")
        sys.exit(1)
    elif input_file.split(".")[-1] != "csv" or output_file.split(".")[-1] != "csv":
        print("Input and output file must be .csv")
        sys.exit(1)
    elif preferred_names and preferred_names.split(".")[-1] != "json":
        print("Preferred names file must be .json")
        sys.exit(1)
    else:
        print("Input file: " + input_file)
        print("Output file: " + output_file)
        print("Starting transfer process...")
        transfer(input_file, output_file, preferred_names)