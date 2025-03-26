from packages.animal_management.min_animal_menu import min_animal_menu_mam, min_animal_menu_bird

def main():
    print("Welcome to the Edinburgh Zoo Management System. Use the menu below to navigate through the system :) Thank you!")
    print("The following actions and options are available:\n"
        "1. Go to the Mammals Catalogue.\n"
        "2. Go to the Birds Catalogue.\n"
        "3. Display all animal details.\n"
        "4. Add an animal to the Zoo's Catalogue.\n"
        "5. Make all animal noises for the animals in the Zoo.\n"
        "6. Exit.")
    
def mam_menu():
    print("Welcome to the Mammal's menu. The following actions are available:")
    min_animal_menu_mam()

def bird_menu():
    print("Welcome to the Bird's menu. The following actions are available:")
    min_animal_menu_bird()

def add_animal():
    print("WELCOME TO THE ADD AND ANIMAL MENU. SPECIFY WHICH ANIMAL IS TO BE ADDED:")
    print("1. Mammals.")
    print("2. Birds.")
    print("3. Exit.")
    