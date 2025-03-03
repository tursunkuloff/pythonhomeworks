import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, 'w').close()

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!")

    def view_employees(self):
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
        
        if not employees:
            print("No records found.")
        else:
            print("Employee Records:")
            for emp in employees:
                print(emp.strip())

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        updated_records = []
        found = False

        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()

        for line in employees:
            if line.startswith(employee_id + ","):
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                updated_records.append(f"{employee_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(line)

        if found:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        updated_records = []
        found = False

        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()

        for line in employees:
            if not line.startswith(employee_id + ","):
                updated_records.append(line)
            else:
                found = True

        if found:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nEmployee Records Manager")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
