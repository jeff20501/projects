class Employee:
    def __init__(self, name, salary, position):
        self.name=name
        self.salary=salary
        self.position=position
    
    def display_employee_details(self):
        raise NotImplementedError("Each subclass need to implement this method!")
    
    def calculate_annual_salary(self):
        return self.salary*12
    
class Full_time(Employee):
    def __init__(self, name, salary, position, health_sub):
        super().__init__(name, salary, position)
        self.health_sub=health_sub
    
    
    def display_employee_details(self):
        print(f"Full-Time Employee: {self.name}\n" 
              f"Position: {self.position}\n"
              f"Salary: {self.salary}\n"
              f"Health subscribtion: {self.health_sub}\n"
              f"{'-'*100}")
        
    def calculate_annual_salary(self):
        return super().calculate_annual_salary()
    
    def health_insurance(self, name):
        print(f"* The employee {self.name}\n"  
              f"* Weekly health insuarnce subscribtion of {self.health_sub}\n"
              f"{'-'*100}")

class Part_time(Employee):
    def __init__(self, name, salary, position, work_hours):
        super().__init__(name, salary, position)
        self.work_hours=work_hours
    
    def display_employee_details(self):
        print(f"Part-Time Employee: {self.name}\n"
              f"Position: {self.position}\n"
              f"Salary: {self.salary}\n"
              f"Working hours: {self.work_hours}\n"
              f"{'-'*100}")
        
    def calculate_annual_salary(self):
        return self.salary*self.work_hours
    
    def hours_weekly(self, name):
        print(f"The Part time employee {self.name}\n"
              f"works {self.work_hours} hours per week.\n"
              f"{'-'*100}")


class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"The employee {employee.name} has sucessfully being added\n"
              f"{':)'*10}")
    
    def calculate_payroll(self):
        # This calculate the money the compay uses to pay it's employees
        total_payroll = sum(emp.calculate_annual_salary() for emp in self.employees) #emp stands for employee
        return total_payroll
    
    def display_all_employee_details(self):
        for emp in self.employees:
            emp.display_employee_details()
