from packages.classes import Animal, Mammal, Bird, Zoo
from packages.menu import main, mam_menu, bird_menu, add_animal
from packages.add_animal import add_mam, add_bird
import time  # Import time module for delay for playing the audio when user wants to hear all of them at once

def main_fun():
    animals = [
        Mammal(name = "Lion", species = "Panthera leo", age= "10 to 14 years in the wild, up to 20 years in captivity" , sound_file=r"C:\Users\Admin\OneDrive\Documents\Code\Zoo Management System\sounds\Lion.mp3", fur_color= "Golden-yellow", habitat= "Grasslands, savannas, and open woodlands"),
        Mammal(name = "Arctic Fox",  species = "Vulpes lagopus", age = "3 to 6 years in the wild, up to 14 years in captivity", sound_file =r"C:\Users\Admin\OneDrive\Documents\Code\Zoo Management System\sounds\Arctic_Fox.mp3", fur_color=" White in winter, brownish-gray in summer", habitat="Arctic tundra and coastal areas"),
        Bird(name="Bald Eagle", species="Haliaeetus leucocephalus", age=" 20 to 30 years in the wild, up to 50 years in captivity", sound_file=r"C:\Users\Admin\OneDrive\Documents\Code\Zoo Management System\sounds\Bald_eagle.mp3", wingspan="1.8 to 2.3 meters (5.9 to 7.5 feet)", beak_type="Hooked and strong for tearing meat"),
        Bird(name="Kingfisher", species="Alcedo atthis", age="6 to 10 years in the wild", sound_file=r"C:\Users\Admin\OneDrive\Documents\Code\Zoo Management System\sounds\kingfisher.mp3", wingspan="25 to 30 cm (9.8 to 11.8 inches)", beak_type="Long and pointed for catching fish"),
    ]
    
    zoo = Zoo() # Usng composition
    # Composition involves building classes that contain instances of other classes, rather than inheriting from them.
    
    while True:
        main()
        try:
            choice =  int(input("Enter the operation you want to do: "))
            if choice == 1:
                mam_menu()
                try:
                    mam_choice=int(input("Enter the operation you want to do: "))
                    if mam_choice==1:
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if isinstance(ani, Mammal):
                                print(ani.display_details())
                                found = True  # Mark as found
                                break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    elif mam_choice==2:
                        make_sound_mam=input("Enter the Mammal you want to hear the sound they make: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == make_sound_mam:
                                found = True  # Mark as found
                                break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    
                    elif mam_choice==3:
                        fur_color=input("Enter the name of the animal you want to know it's fur color: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == fur_color:    
                                if isinstance(ani, Mammal):
                                    print(ani.display_fur_color())
                                    found = True  # Mark as found
                                    break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    
                    elif mam_choice==4:
                        habitat=input("Enter the name of the animal you want to know its habitat: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == habitat:
                                if isinstance(ani, Mammal):
                                    print(ani.display_habitat())
                                found = True  # Mark as found
                                break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    elif mam_choice==5:
                        print("Thank you for choosing us goodbye!\n"
                              f"{'-'*100}")
                        break
                    
                    else:
                        print("Invalid input Enter either 1,2,3,4 or 5 to exit the Mammals menu!\n"
                              f"{'-'*100}")
                
                except  ValueError:
                    print("Enter a number as represented by the choices given!\n"
                              f"{'-'*100}")
            
            
            elif choice == 2:
                bird_menu()
                try:
                    bird_choice=int(input("Enter the operation you want to do: "))
                    if bird_choice==1:
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                             if isinstance(ani, Bird):
                                print(ani.display_details())
                                found = True  # Mark as found
                                break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    
                    elif bird_choice==2:
                        make_sound_bird=input("Enter the bird you want to hear the sound they make: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == make_sound_bird:
                                if isinstance(ani, Bird):
                                    ani.play_sound()
                                    found = True  # Mark as found
                                    break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    
                    elif bird_choice==3:
                        wing_span=input("Enter the Bird you want to know there wing span: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == wing_span:
                                if isinstance(ani, Bird):
                                    print(ani.display_wingspan())
                                    found = True  # Mark as found
                                    break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!\n"
                              f"{'-'*100}")
                    
                    elif bird_choice==4:
                        beak_type=input("Enter the name of the Bird you want to know the beak type: ")
                        found = False # avoid an UnboundLocalError when found is referenced in the if not found: check
                        for ani in animals:
                            if ani.name == beak_type:
                                if isinstance(ani, Bird):
                                    print(ani.display_beak_type())
                                    found = True  # Mark as found
                                    break  # Stop looping once found

                        if not found:
                            print("There is no animal with that name in our logs!")
                    elif bird_choice == 5:
                        print(f"Thank for your vist see you next time! {":)"*10}\n"
                              f"{'-'*100}")
                        break
                    
                    else:
                        print("Invalid input Enter either 1,2,3,4 or 5 to exit the Mammals menu!\n"
                              f"{'-'*100}")
                
                except ValueError:
                    print("Enter a number as represented by the choices given!\n"
                              f"{'-'*100}")
            
            elif choice==3:
                found = False # so as to avoid a  UnboundLocalError
                for ani in animals:
                       if isinstance(ani, Mammal) or isinstance(ani, Bird): # used or instead of and since and a single object can not be both a Mammal and a Bird at the same time
                           print(ani.display_details())
                           found=True
                
                if not found:
                    print("Currently no animals in our Zoo!")
                            
            elif choice==4:
                add_animal()
                try:    
                    add_ani_choice=int(input("Enter the Kind of animal you want to add to the zoo: "))
                    if add_ani_choice==1:
                        new_mammal=add_mam()
                        zoo.add_animal(new_mammal) # Using composition instead of inheriting!!!
                    
                    elif add_ani_choice==2:
                        new_bird=add_bird()
                        zoo.add_animal(new_bird)
                    
                    elif add_ani_choice==3:
                        print("Goodbye!!")
                        break
                    
                    else:
                        print("Invalid input! Enter either 1,2 or 3 to exit!\n"
                              f"{'-'*100}")
                
                except ValueError:
                    print("Invalid input. Enter the choice as presented in the choice eg. 1,2...\n"
                        f"{'-'*100}")
            
            elif choice == 5:
                found = False
                for ani in animals:
                    if ani.sound_file:  # Check if sound_file exists (not None or empty)
                        found = True
                        ani.play_sound()  # Play the sound for the matching animal
                        time.sleep(5)  # Add delay (5 seconds) to let the sound play
                
            elif choice == 6:
                print("Have a nice day see you soon!\n"
                              f"{'-'*100}")
                break
            else:
                print("Invalid input enter either 1,2,3,4,5 or 6 to exit!")
        
        except ValueError:
            print("Invalid input. Enter the choice as presented in the choice eg. 1,2...")

if __name__ == "__main__": #This script will only run if it is run directly it should not be imported!
    main_fun()
                    