from functions.calculate_gpa import calculate_GPA_func, display_GPA_func
class Student:
    def __init__(self, name, student_id):
        self.name=name
        self.student_id=student_id
    
    def display_student_details(self):
        raise NotImplementedError("Each subclass need to implement this method!")
    
    def calculate_GPA(self):
        raise NotImplementedError("Each subclass need to implement this method!")
    
class Undergraduate(Student):
    def __init__(self, name, student_id, major, year_of_study):
        super().__init__(name, student_id)
        self.major = major
        self.year_of_study = year_of_study
    
    def display_student_details(self):
        print(f"Undergraduate: {self.name}  Student ID: {self.student_id}  Major: {self.major}  Year: {self.year_of_study}")
        
    def calculate_GPA(self, student_id):
        print(f"The Undergraduate student {self.name} Student ID {self.student_id} GPA: {calculate_GPA_func()}")
    
    def display_GPA(self):
        print(f"The UNdergraduate student {self.name} Student ID {self.student_id} GPA: {display_GPA_func()}")
    
class Graduate(Student):
    def __init__(self, name, student_id, thesis_topic, advisor):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        self.advisor = advisor
    
    def display_student_details(self):
        print(f"Graduate: {self.name}  Student ID: {self.student_id}  Thesis Topic: {self.thesis_topic}  Advisor: {self.advisor}")
    
    def calculate_GPA(self):
        print(f"The Graduate Student {self.name} Student ID {self.student_id} has a GPA of {calculate_GPA_func()}")
    
    def display_GPA(self):
        print(f"The Graduate student {self.name} Student ID {self.student_id} GPA: {display_GPA_func()}")
class Course:
    def __init__(self):
        self.students=[]
        
    def add_students(self, student):
        self.students.append(student)
        print(f"The student {student.name} Student ID {student.student_id} has been added succesfully!!")
    
    def calculate_avarage_GPA(self):
        average_gpa = sum(stu.calculate_GPA_func() for stu in self.students) #stu stands for student
        return average_gpa
    
    def display_details_all_students(self):
        for stu in self.students:
            stu.display_student_details()
          