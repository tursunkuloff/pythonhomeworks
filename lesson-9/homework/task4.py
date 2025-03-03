import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {status}, Priority: {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def modify_task(tasks):
    task_id = int(input("Enter the ID of the task to modify: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = input("Mark as completed? (yes/no): ").strip().lower() == "yes"
            task["priority"] = int(input("Enter new priority: "))
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

# Main Execution
tasks = load_tasks()
display_tasks(tasks)
calculate_stats(tasks)

if input("Modify a task? (yes/no): ").strip().lower() == "yes":
    modify_task(tasks)