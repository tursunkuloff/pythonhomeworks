import json
import csv

def convert_json_to_csv(json_file, csv_file):
    # Load JSON data
    with open(json_file, "r") as file:
        tasks = json.load(file)

    # Write to CSV
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])  # Header
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

    print(f"Tasks successfully converted to {csv_file}.")

# Convert tasks.json to tasks.csv
convert_json_to_csv("tasks.json", "tasks.csv")
