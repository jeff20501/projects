import pygame  # Library to play sounds

try:
    pygame.mixer.init()  # This starts the audio system

except pygame.mixer.error as e:  # If there's an issue, handle it
    print(f"Audio system error: {e}")  # Print out the error message
    pygame_audio_enabled = False  # Disable sound functionality

else:
    pygame_audio_enabled = True  # Sound system is working fine

class Animal:
    def __init__(self, name, species, age, sound_file):
        self.name=name
        self.species=species
        self.age=age
        self.sound_file=sound_file  # Stores the file path of the animal's sound
    
    def display_details(self):
        raise NotImplementedError("Each subclass need to implement this method!")    
    
    def play_sound(self): # Defines a method to play the sound.
        """Plays the animal's sound file"""
        pygame.mixer.music.load(self.sound_file) #Loads the sound file into memory.
        pygame.mixer.music.play() # play the sound



class Mammal(Animal):
    def __init__(self, name, species, age, sound_file, fur_color, habitat):
        super().__init__(name, species, age, sound_file)
        self.fur_color=fur_color
        self.habitat=habitat
    
    def display_details(self):  # Implements the method as required
        return (f"Name: {self.name}\n"
                f"Species: {self.species}\n"
                f"Age: {self.age}\n"
                f"Sound: {self.sound_file}\n"
                f"Fur Color: {self.fur_color}\n"
                f"Habitat: {self.habitat}\n"
                f"{'-' * 50}")
    
    def display_fur_color(self):
        return f"The fur color of {self.name} is {self.fur_color}"
    
    def display_habitat(self):
        return f"The habitat of the {self.name} is {self.habitat}" 


class Bird(Animal):
    def __init__(self, name, species, age, sound_file, wingspan, beak_type):
        super().__init__(name, species, age, sound_file)
        self.wingspan=wingspan
        self.beak_type=beak_type
    
    def display_details(self):  # Bird-specific implementation
         return (f"Name: {self.name}\n"
                 f"Species: {self.species}\n"
                 f"Age: {self.age}\n"
                 f"Sound: {self.sound_file}\n"
                 f"Wingspan: {self.wingspan}\n"
                 f"Beak Type: {self.beak_type}\n"
                 f"{'-' * 100}")
    
    def display_wingspan(self):
        return (f"The bird {self.name} has a wing span of {self.wingspan}\n"
                f"{'-'*50}")
    
    def display_beak_type(self):
        return f"The Bird {self.name} has the beak type {self.beak_type}"

class Zoo:
    def __init__(self):
        self.animals=[]
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"The animal {animal.name} has been added to the logs")
    

            
            
    