import csv
from collections import defaultdict

def read_grades(filename):
    grades = defaultdict(list)
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])
            grades[subject].append(grade)
    return grades

def calculate_averages(grades):
    averages = {subject: sum(grades_list) / len(grades_list) for subject, grades_list in grades.items()}
    return averages

def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

def main():
    input_file = "grades.csv"
    output_file = "average_grades.csv"
    
    grades = read_grades(input_file)
    averages = calculate_averages(grades)
    write_averages(output_file, averages)
    
    print("Average grades have been written to", output_file)

if __name__ == "__main__":
    main()