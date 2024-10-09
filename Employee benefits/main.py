from packages.menu import main_menu, full_time_menu, part_time_menu
from packages.classes import Employee, Full_time, Part_time, Department

def main():
    full_time_employee_list = [
        Full_time(name='JEFF', position='Manager', salary=200000, health_sub=20000),
        ]
    part_time_employee_list = [
        Part_time(name='JACK', position='Intern', salary=10000, work_hours=35)
    ]
    department = Department()  # Usng composition
    # Composition involves building classes that contain instances of other classes, rather than inheriting from them. This means that instead of a Department being a subclass of Full_time and Part_time, it would contain instances of Full_time and Part_time.

    while True:
        main_menu()
        try:
            choice=int(input("Input the action you want to do: "))
            if choice == 1:          
                full_time_menu()
                try:
                    choice2=int(input("Input the option you have decided to do: "))
                    if choice2 == 1:
                        for employee in full_time_employee_list:
                            employee.display_employee_details()
                            print()
                            if not employee:
                                print("There are currently no employees in this type!")

                    elif choice2 == 2:
                        full_time_employee_name_salary = input("Enter the name of the employee: ")
                        for employee in full_time_employee_list:
                            if employee.name == full_time_employee_name_salary.upper():
                                print(f"The employee  {full_time_employee_name_salary} has an yearly salary of {employee.calculate_annual_salary()}")
                                break
                            else:
                                print(f"There is no such employee with this name ( {employee} ).")                            
                    elif choice2 == 3:
                        full_time_employee_name_health_sub = input("Enter the employee's name: ")
                        for employee in full_time_employee_list:
                            employee.health_insurance(full_time_employee_name_health_sub)
                            if not employee:
                                print(f"There is no employee with the name ( {full_time_employee_name_health_sub} ).")
                    elif choice2 == 4:
                        print("SEE YOU AGAIN NEXT TIME!")
                        break
                    
                    else:
                        print("Invalid input!! Enter either 1, 2 or 3 to exit")
                        
                except ValueError:
                            print('Enter a number as represented by the choices given!')
            
            elif choice ==2:
                part_time_menu()
                try:
                    choice3=int(input("Input the option you have decided to do: "))
                    if choice3 == 1:
                        for employee in  part_time_employee_list:
                            employee.display_employee_details()
                            print()
                            if not employee:
                               print("There are currently no employees in this type!")

                    elif choice3 == 2:
                        part_time_employee = input("Enter the name of the employee: ")
                        for employee in part_time_employee_list:
                            if employee.name == part_time_employee.upper():
                                print(f"The employee {part_time_employee} has an yearly salary of {employee.calculate_annual_salary()}")
                                break
                            else:
                                print(f"There is no such employee with this name ( {part_time_employee} ).")                            
                    elif choice3 == 3:
                        employee_name2 = input("Enter the employee's name: ")
                        for employee in part_time_employee_list:
                            if not employee:
                                print(f"There is no employee with the name ( {employee_name2} ).")
                            else:
                                employee.hours_weekly(employee_name2)
                                break
                    elif choice2 == 4:
                        print("SEE YOU AGAIN NEXT TIME!")
                        break
                    else:
                        print("Invalid input!! Enter either 1, 2 or 3 to exit")
                        
                except ValueError:
                            print('Enter a number as represented by the choices given!')         
            
            elif choice == 3:
                new_employee_name = input("Enter the name of the employee: ").upper()
                employee_position = input("Enter the position the employee will occupy: ")
                employee_salary = int(input("Enter the stating salry of this employee: "))
                new_employee_type = input("What will be the type of employee (Full time or Part time): ")
                
                if new_employee_type.lower() == 'full time':
                    try:
                        employee_health_insuarance_sub = int(input("Input the health subscribtion of the Employee: "))
                        new_full_time_employee = Full_time(new_employee_name, employee_salary, employee_position, employee_health_insuarance_sub)
                        department = Department()   
                        department.add_employee(new_full_time_employee)  # Using composition instead of inheriting!!!
                    except ValueError:
                        print("Enter a number for the price of the Health Insuarance subscribtion!!")
                                
                elif new_employee_type.lower() == 'part time':
                    try:
                        part_time_employee_working_hours = int(input("Enter the working hours of the Part time employee for every month: "))
                        new_part_time_employee = Part_time(new_employee_name, employee_position, employee_salary, part_time_employee_working_hours)
                        department.add_employee(new_part_time_employee)  # Using composition instead of inheriting!!!
                    except ValueError:
                        print("Enter a Number for the number of hours!!")
                
                else:
                    print("Invalid Input!")
                    
                    
            elif choice == 4:
                name_of_employee = input("Enter the name of the employee you want to know the payroll for an year: ")
                for employee in department.employees:  # Use department's employee list
                    if employee.name == name_of_employee.upper():
                        print(f"{employee.name}'s annual salary is: {employee.calculate_annual_salary()}")
                        break
                else:
                    print("There is no employee with that name!!")
            elif choice ==5:
                    department.display_all_employee_details()
                    print()
                    
            elif choice==6:
                print("See you next time. Goodbye!")
                break
            
            else:
                print("Invalid input!! Enter either 1, 2,3,4,5 or 6 exit")      
        
        except ValueError:
            print("Enter a number as showed in the options!!")
            
if __name__ == "__main__": #This script will only run if it is run directly it should not be imported!
    main()              
                        
                                                 
                
                        
                                                    
                                    
                                