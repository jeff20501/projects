class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    
    
    def details(self):
        raise NotImplementedError("Each Subclass should implement this method!")
    
    def age(self, current_year): # we don't initiate current year since we only need it to do one thing
        return current_year - self.year

class Car(Vehicle):
    def __init__(self, number_of_doors, make, model, year):
        super().__init__(make, model, year)
        self.number_of_doors= number_of_doors
        
    def details(self):
        print(f"Car: {self.make}\n" 
              f"Model: {self.model}\n" 
              f"Year of manufacture: {self.year}\n" 
              f"NUmber of doors: {self.number_of_doors} doors.\n"
              f"{'-'*100}")
    
    def age(self, current_year):
        return super().age(current_year)
    
class Truck(Vehicle):
    def __init__(self, cargo_capacity, make, model, year):
        super().__init__(make, model, year)
        self.cargo_capacity=cargo_capacity
    
    def details(self):
        print(f"Truck: {self.make}\n"
              f"Model: {self.model}\n "
              f"Year of Manufacture: {self.year}\n" 
              f"Capacity {self.cargo_capacity} tons.\n"
              f"{'-'*100}")
    
    def age(self, current_year):
        return super().age(current_year)
    
    

