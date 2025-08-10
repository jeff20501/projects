#EmployeeMS
class Employee:
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary
        
    def details(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def bonuses(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Manager(Employee):
    def __init__(self, department):
        self.department = department
        self.employee = {
            'HR' : Employee('Jefferson', 90000) 
        }
    
    def details(self):
        
        if not self.employee:
            print("There are currently no employees in this employee type!")
        else:
            for key, value in self.employee.items():
                print(f'the department {key} has {value.name} with a salary of {value.salary}')
                print()
    
    def bonuses(self,  percentage):
        salary=90000
        bonus = percentage/100 * salary
        salary+=bonus
        print(f"You salary was increased by a percentage of {percentage:.2f}% your salary is now {salary}")
        

class Developer(Employee):
    def __init__(self, programming_language):
        self.programming_language = programming_language
        self.employee = {
            'Python': Employee('Jake', 60000)
        }
    
    def details(self):
        if not self.employee.keys():
            print("There are currently no employees in this employee type!")
        else:
            for key, value in self.employee.items():
                print(f'{key} is from the department {value.name} with a salary of {value.salary}')
                print()
    
    def bonuses(self,percentage):
        salary=60000
        bonus = percentage/100 * salary
        salary+=bonus
        for key, value in self.employee.items():
            print(f"The salary of {value.name} of the department {key} was increased by a percentage of {percentage:.2f}% your salary is now {salary:.2f}")
        
        
while True:
    print("Welcome to the Employee Management System.")
    print("The following employee types are availble:")
    print("1. Manager")
    print("2. Developer")
    print("3. Exit")
    choice = int(input("What do you want to look at:"))
    
    if choice == 1:
        department = input("Enter the Department: ")
        employee = Manager( department)
        
        while True:
            print("The following operations are available:")
            print("1. Get Details.")
            print("2. Calculate bonuses")
            print("3. Exit")
            
            choice2 = int(input("Which operation do you want to do: "))
            
            if choice2 == 1:
                employee.details()
            
            elif choice2 == 2:
                percentage = float(input("What percentage do you want to increase their salary: "))
                employee.bonuses(percentage)
            
            elif choice2 == 3:
                print("See you later!")
                print()
                break
            
            else: 
                print("Invalid input enter either 1,2 or 3 to exit")
                continue
    
    if choice == 2:
        programming_language = input("Enter the Programming Language of the employee: ")
        employee = Developer(programming_language)
        while True:
            print("The following operations are available:")
            print("1. Get Details.")
            print("2. Calculate bonuses")
            print("3. Exit")
            
            choice2 = int(input("Which operation do you want to do: "))
            
            if choice2 == 1:
                employee.details()
            
            elif choice2 == 2:
                percentage = float(input("What percentage do you want to increase their salary: "))
                employee.bonuses(percentage)
            
            elif choice2 == 3:
                print("See you later!")
                print()
                break
            
            else: 
                print("Invalid input enter either 1,2 or 3 to exit")
    
    if choice == 3:
        print("See you later!")
        break