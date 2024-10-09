class Employee:
    @classmethod
    
    def create_from_string(cls, name, position, salary):
        return f"The employee Intialized Name: {name} Position: {position} Salary: {salary}"
    
    @staticmethod
    
    def is_valid_salary(valid_salary):
        if valid_salary <= 0:
            return f"The salary {valid_salary} is not valid!!"
        else:
            return f"The salary {valid_salary} is valid!!"

def employee():
    print("We now create an instance of an employee. Just follow the instructions that follow. Thank you!")
    employee_name = input("Enter the name of the employee: ")
    employee_position = input("Enter the position of the employee is in: ")
    while True: # loop untill a valid salary is entered
        try:
            employee_salary = int(input("Enter the salary of the employee:"))
            break # exit loop after a valid salary has been entered
        except (ValueError, NameError, TypeError) as err:
            print(f"{err}")
    return employee_name, employee_position, employee_salary

def main():
    employee_name, employee_position, employee_salary = employee()
    # we directly call the class and static method from the class
    print(Employee.create_from_string(employee_name, employee_position, employee_salary))
    print(Employee.is_valid_salary(employee_salary))

if __name__ == '__main__':
    main()      
    