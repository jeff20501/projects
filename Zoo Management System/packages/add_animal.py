from packages.classes import Mammal, Bird
def add_mam():
    print("Enter the details of the Mammal you want to add follow the instructions below: ")
    new_mam_name=input("Enter the name of the Mammal: ")
    new_mam_species=input("Enter it's Species: ")
    new_mam_age=input("Enter the age: ")
    new_mam_sound_file=input("Enter the sound file of the sound of the Mammal: ")
    new_mam_fur=input("Enter the color of fur: ")
    new_mam_habitat=input("Enter the habitat of the Mammal: ")
    return Mammal(new_mam_name, new_mam_species, new_mam_age, new_mam_sound_file,  new_mam_fur, new_mam_habitat)

def add_bird():
    print("Enter the details of the Bird you want to add follow the instructions below: ")
    new_bird_name=input("Enter the name of the Mammal: ")
    new_bird_species=input("Enter it's Species: ")
    new_bird_age=input("Enter the age: ")
    new_bird_sound_file=input("Enter the sound file of the sound of the Bird: ")
    new_bird_wingspan=input("Enter the wingspan: ")
    new_bird_beak_type=input("Enter the beak type of the Mammal: ")
    return Bird(new_bird_name, new_bird_species, new_bird_age, new_bird_sound_file,  new_bird_wingspan, new_bird_beak_type)