class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, job, salary):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
        else:
            self.employees[emp_id] = {'Name': name, 'Job': job, 'Salary': salary}
            print(f"Employee {name} added.")

    def print_employee(self, emp_id):
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            print(f"ID: {emp_id}, Name: {employee['Name']}, Job: {employee['Job']}, Salary: {employee['Salary']}")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} removed.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, name=None, job=None, salary=None):
        if emp_id in self.employees:
            if name is not None:
                self.employees[emp_id]['Name'] = name
            if job is not None:
                self.employees[emp_id]['Job'] = job
            if salary is not None:
                self.employees[emp_id]['Salary'] = salary
            print(f"Employee with ID {emp_id} updated.")
        else:
            print(f"Employee with ID {emp_id} not found.")

def main():
    db = EmployeeDatabase()
    while True:
        print("\nEmployee Database System")
        print("1. Add new employee")
        print("2. Print employee data")
        print("3. Remove employee from the system")
        print("4. Update employee data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            job = input("Enter employee job: ")
            salary = input("Enter employee salary: ")
            db.add_employee(emp_id, name, job, salary)
        elif choice == '2':
            emp_id = input("Enter employee ID: ")
            db.print_employee(emp_id)
        elif choice == '3':
            emp_id = input("Enter employee ID: ")
            db.remove_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter employee ID: ")
            name = input("Enter new name (leave blank to keep current): ")
            job = input("Enter new job (leave blank to keep current): ")
            salary = input("Enter new salary (leave blank to keep current): ")
            db.update_employee(emp_id, name if name else None, job if job else None, salary if salary else None)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
