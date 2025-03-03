import json
import csv
from abc import ABC, abstractmethod

# Abstract class for file handling
class TaskStorage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

# CSV Storage Implementation
class CSVStorage(TaskStorage):
    def __init__(self, filename='tasks.csv'):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task ID', 'Title', 'Description', 'Due Date', 'Status'])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self):
        tasks = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(row['Task ID'], row['Title'], row['Description'], row['Due Date'], row['Status']))
        except FileNotFoundError:
            pass
        return tasks

# JSON Storage Implementation
class JSONStorage(TaskStorage):
    def __init__(self, filename='tasks.json'):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file)

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return [Task(**data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

# Task Class
class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

# Task Manager
class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save(self.tasks)

    def view_tasks(self):
        for task in self.tasks:
            print(f'{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}')

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                self.storage.save(self.tasks)
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.storage.save(self.tasks)

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status.lower() == status.lower()]

# Example Usage
if __name__ == "__main__":
    storage = JSONStorage()  # Change to CSVStorage() for CSV
    manager = TaskManager(storage)

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Filter Tasks\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(Task(task_id, title, description, due_date, status))
        
        elif choice == '2':
            manager.view_tasks()
        
        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            title = input("New Title (leave blank to keep current): ") or None
            description = input("New Description (leave blank to keep current): ") or None
            due_date = input("New Due Date (leave blank to keep current): ") or None
            status = input("New Status (Pending/In Progress/Completed, leave blank to keep current): ") or None
            manager.update_task(task_id, title, description, due_date, status)
        
        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
        
        elif choice == '5':
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            filtered = manager.filter_tasks(status)
            for task in filtered:
                print(f'{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}')
        
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
