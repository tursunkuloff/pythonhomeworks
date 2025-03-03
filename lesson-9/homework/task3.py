import json

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks back to JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    print("\nTask List:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {status}, Priority: {task['priority']}")

# Modify a task
def modify_task(tasks, task_id, new_status=None, new_priority=None):
    for task in tasks:
        if task["id"] == task_id:
            if new_status is not None:
                task["completed"] = new_status
            if new_priority is not None:
                task["priority"] = new_priority
            return True
    return False

# Main execution
tasks = load_tasks()
display_tasks(tasks)

# Example modification
modify_task(tasks, task_id=3, new_status=True, new_priority=2)
save_tasks(tasks)

display_tasks(tasks)