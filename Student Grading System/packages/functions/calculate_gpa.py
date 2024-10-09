def GPA():
    print("You will now enter the individual Grade point of each course.")
    # we declare the following are going to be global variables
    global course1 
    global course2 
    global course3  
    course1 = input("Enter the grade point of the first course: ").split()
    course2 =  input("Enter the grade point of the second course: ").split()
    course3  = input("Enter the grade point of the second course: ").split()
    print()
    
    print("You will now enter the individual Credit Hours of each course.")
    global credit_hours1
    global credit_hours2
    global credit_hours3
    credit_hours1 = input("Enter the credit hours for the first course (Make sure the credit hours are for the first course you entered!!! )")
    credit_hours2 = input("Enter the credit hours for the second course (Make sure the credit hours are for the second course you entered!!! )")
    credit_hours3 = input("Enter the credit hours for the third course (Make sure the credit hours are for the third course you entered!!! )")
    print()
    print()
    
def calculate_GPA_func():    
    grade_points = []
    credit_hours_list = []
    
    for point in list(map(int, course1)), list(map(int, course2)), list(map(int, course3)):
        grade_points += point
        
    for hour in list(map(int, credit_hours1)), list(map(int, credit_hours2)), list(map(int, credit_hours3)):
        credit_hours_list += hour
    
    # To calculate the GPA the formula is (sum(grade points * credit hours)) / sum(credit hours) so lets do the below
    
    results = [grade_points[i] * credit_hours_list[i] for i in range(min(len(grade_points), len(credit_hours_list)))]
   
    # using a for loop 
    #results = []
    # for i in range(min(len(grade_points) len(credit_hours_list))):
    #     results.append(grade_points[i] * credit_hours_list[i])
    
    calculated_GPA = sum(results) / sum(credit_hours_list)
    return calculated_GPA

def display_GPA_func():
    return calculate_GPA_func()
    