from packages.menu import main_menu, undergraduate_menu, graduate
from packages.classes import Student, Undergraduate, Graduate, Course
from functions.calculate_gpa import GPA
def main():
    undergraduate_list = [
        Undergraduate(name='JACK', student_id='P100/4035G', year_of_study=2, major='IT'),
        Undergraduate(name='JEFF', student_id='P100/4805G', year_of_study=1, major='CS')
    ]
    
    graduate_list = [
        Graduate(name='LUCY', student_id='B102/4564G', thesis_topic='Micro_biology', advisor='Dr. Jane'),
        Graduate(name='MARY', student_id='P104/4230G', thesis_topic='Q.Physics', advisor='Dr. Jane')        
    ]
    
    course = Course()
    
    while True:
        main_menu()
        try:
            choice = int(input("Enter the action you want to do: "))
            if choice == 1:
                undergraduate_menu()
                try:
                    choice_undergraduate = int(input("Enter the action you want to under take: "))
                    if choice_undergraduate == 1:
                        for student in undergraduate_list:
                            student. display_student_details()
                            print()
                            if not student:
                                print("There is no Undergraduate student in this institution at this time!!")
                    
                    elif choice_undergraduate == 2:
                        undergraduate_student_id_GPA = input("Enter the student ID of the student you want to calculate there GPA: ")
                        for student in undergraduate_list:
                            if student.student_id == undergraduate_student_id_GPA:
                                GPA()
                                student.calculate_GPA(undergraduate_student_id_GPA)
                                break
                            else:
                                print(f"There is no student with this student ID {undergraduate_student_id_GPA}. KIndly check the ID and try again!!")
                        
                    
                    elif choice_undergraduate == 3:
                        undergraduate_student_id__display_GPA = input("Enter the Student ID of the student you want me to display their GPA: ")
                        for student in undergraduate_list:
                            if student.student_id == undergraduate_student_id__display_GPA:
                                student.display_GPA()
                                break
                    
                    elif choice_undergraduate == 4:
                        print("See you next time!!")
                        break
                
                except ValueError:
                    print("Enter a number as given in the choices!!")
                    
            elif choice == 2:
                graduate()
                try:
                    choice_graduate = int(input("Enter the action you want to under take: "))
                    if choice_graduate == 1:
                        for student in graduate_list:
                            student.display_student_details()
                            print()
                            if not student:
                                print("There is no Graduate student in this institution at this time!!")
                    
                    elif choice_graduate == 2:
                        graduate_student_id_GPA = input("Enter the student ID of the Graduate student: ")
                        for student in graduate_list:
                            if student.student_id == graduate_student_id_GPA:
                                GPA()
                                student.calculate_GPA(graduate_student_id_GPA)
                                break
                            else:
                                print(f"There is no graduate student with this student ID {graduate_student_id_GPA}. Kindly check the ID and Try again!!")
                    
                    elif choice_graduate == 3:
                        graduate_student_id__display_GPA = input("Enter the Student ID of the student you want me to display their GPA: ")
                        for student in graduate_list:
                            if student.student_id == graduate_student_id__display_GPA:
                                student.display_GPA()
                                break
                    
                    elif choice_undergraduate == 4:
                        print("See you next time!!")
                        break
                except ValueError:
                    print("Enter a number as given in the choices!!")
            
            elif choice == 3:
                print("Welcome to the add a student page (NOTE: You can only add Undergraduate Student):")
                new_undergrad_stu_name = input("Enter the name of the Undergraduate student: ")
                new_undergrad_stu_id = input("Enter the Student ID of tthe student: ")
                new_undergrad_stu_year_of_study = int(input("Enter the year of study of the student: "))
                new_undergrad_stu_major = input("Enter the Major of the student: ") 
                new_undergrad_student = Undergraduate(new_undergrad_stu_name, new_undergrad_stu_id, new_undergrad_stu_year_of_study, new_undergrad_stu_major)
                course.add_students(new_undergrad_student)
            
            elif choice == 4:
                print("Welcome> Here you will be able to calculate the average GPA of a student:")
                student_id_know_GPA = input("Enter the student ID of the student: ")
                for student in course.students:
                    if student.student_id ==  student_id_know_GPA:
                        print(f"The student with the ID {student.name} has a GPA of {student. calculate_avarage_GPA()}.")
                        break
                    else:
                        print("There is no student with the student ID given.")
            
            elif choice == 5:
                course.display_details_all_students()
                print()
            
            elif choice == 6:
                print("See you next time!")
                break
            
            else:
                print("Choose and enter either 1,2,3,4,5 or 6 to exit!")
        
        except ValueError:
            print("Enter a number as shown by the choices!!")
            

if __name__ == "__main__":
    main()        
                        
                                               