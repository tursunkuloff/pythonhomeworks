def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        record = f"{emp_id}, {name}, {position}, {salary}"
        file.write(record + "\n")
        print("Employee record added successfully.")
        print("Recorded Employee Information:")
        print(record)

# Run the function to add an employee
add_employee()