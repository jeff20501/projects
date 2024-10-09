from Vehicle_packages.class_veh_menu import main_menu, car_menu, truck_menu
from Vehicle_packages.class_vehicle import Vehicle, Car, Truck
#import the packages
def main():
    #a list of the cars and trucks available
    cars = [
        Car(number_of_doors=2, make='Ferrari', model='Ferrari F8', year=2019),
        Car(number_of_doors=2, make='Nissan', model='Nissan Skyline GT-R ', year=2002),
        Car(number_of_doors=4, make='BMW', model=' BMW M2 Series Gran Coupe', year=2019),
        Car(number_of_doors=2, make='Mercedes', model='Mercedes-AMG GT', year=2014),
        Car(number_of_doors=2, make='Mercedes', model='Mercedes-AMG EQS 53', year=2021)
    ]
    
    trucks = [
        Truck(cargo_capacity=10, make='Isuzu', model='Isuzu FRR', year=2024),
        Truck(cargo_capacity='18 to 26', make='Mercedes-Benz ', model='Actros', year=2019),
        Truck(cargo_capacity=30, make='Scania', model='XT', year=2019)
    ]
    
    while True:
        main_menu() #functions from class_veh_menu
        try:
            choice = int(input('Which vehicle do you want to take action upon: '))
            if choice == 1:
                car_menu()
                try:
                    choice2 = int(input('Choice the action you want to do: '))
                    if choice2 == 1:
                        for car in cars:
                            if not car:
                                print("There are currently no cars in this fleet:")
                            else:
                                car.details()
                                print()
                    
                    elif choice2 == 2:
                        car_model=input('Enter the model of the car:')
                        current_year=int(input('Enter the current year:'))
                        
                        for car in cars:
                            if car.model==car_model:
                                print(f"The car model {car.model} is {car.age(current_year)} year old")
                                break
                            
                            else:
                                print("We currently don\'t have this model!")
                    
                    elif choice2 == 3:
                        print("You have exited this menu!")
                        break
                    else:
                        print("Invalid input! Kindly enter either 1,2 or 3 to exit")
                except  ValueError:
                    print('Enter a number as represented by the choices given!')
            
            elif choice == 2:
                truck_menu()
                try:
                    choice2 = int(input('Choice the action you want to do: '))
                    if choice2 == 1:
                        for truck in trucks:
                            if not truck:
                                print("There are currently no trucks in this fleet:")
                            else:
                                truck.details()
                    
                    elif choice2 == 2:
                        truck_model=input('Enter the model of the truck:')
                        current_year=int(input('Enter the current year:'))
                        
                        for car in cars:
                            if truck.model==truck_model:
                                print(f"The truck model {truck.model} is {truck.age(current_year)} year old.")
                                break
                            
                            else:
                                print("We currently don\'t have this model!")
                    
                    elif choice2 == 3:
                        print("You have exited this menu!")
                        break
                    else:
                        print("Invalid input! Kindly enter either 1,2 or 3 to exit")
                except  ValueError:
                    print('Enter a number as represented by the choices given!')
            
            elif choice == 3:
                print("Thank you for visiting us today, See you next time!")
                break
            else:
                print("Invalid input! Kindly enter either 1,2 or 3 to exit")
        
        except ValueError:
            print('Enter a number as represented by the choices given!')        
                        
if __name__ == "__main__": #This script will only run if it is run directly it should not be imported!
    main()
                    
