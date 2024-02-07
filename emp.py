import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}\nID: {self.emp_id}\nTitle: {self.title}\nDepartment: {self.department}\n")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, ID: {employee.emp_id}")

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added successfully.")
        else:
            print(f"Department '{department_name}' already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed successfully.")
        else:
            print(f"Department '{department_name}' does not exist.")

    def display_departments(self):
        print("Departments:")
        for department_name in self.departments:
            print(f"- {department_name}")

    def save_to_file(self, filename):
        data = {
            'departments': {
                name: {'employees': [emp.__dict__ for emp in dept.employees]} for name, dept in self.departments.items()
            }
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for department_name, department_data in data['departments'].items():
                    department = Department(department_name)
                    for employee_data in department_data['employees']:
                        employee = Employee(**employee_data)
                        department.add_employee(employee)
                    self.departments[department_name] = department
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")

def print_menu():
    print("\nMenu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Display Departments")
    print("4. Add Employee")
    print("5. Remove Employee")
    print("6. List Employees in Department")
    print("7. Save Data to File")
    print("8. Load Data from File")
    print("9. Quit")

def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            department_name = input("Enter the department name: ")
            company.add_department(department_name)

        elif choice == '2':
            department_name = input("Enter the department name: ")
            company.remove_department(department_name)

        elif choice == '3':
            company.display_departments()

        elif choice == '4':
            department_name = input("Enter the department name: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                employee = Employee(name, emp_id, title, department_name)
                company.departments[department_name].add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '5':
            department_name = input("Enter the department name: ")
            if department_name in company.departments:
                emp_id = input("Enter employee ID to remove: ")
                department = company.departments[department_name]
                employees = department.employees
                for employee in employees:
                    if employee.emp_id == emp_id:
                        department.remove_employee(employee)
                        print("Employee removed successfully.")
                        break
                else:
                    print(f"Employee with ID '{emp_id}' not found.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '6':
            department_name = input("Enter the department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '7':
            filename = input("Enter the filename to save data: ")
            company.save_to_file(filename)

        elif choice == '8':
            filename = input("Enter the filename to load data: ")
            company.load_from_file(filename)

        elif choice == '9':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
