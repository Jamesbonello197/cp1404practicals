"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_details = load_data(FILENAME)
    print_subject_details(subject_details)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        details = [parts[0], parts[1], int(parts[2])]
        subject_details.append(details)
    input_file.close()
    return subject_details


def print_subject_details(subject_details):
    for subject_code, teacher, student_count in subject_details:
        print(f"{subject_code} is taught by {teacher} and has {student_count} students")


main()
