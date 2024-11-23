import pyfiglet
import random
from pygame.base import init
from tqdm import tqdm
import time
from pydub import AudioSegment
from pydub.playback import play
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the .wav file
pygame.mixer.music.load("song.wav")

# Play the music
pygame.mixer.music.play(-1) 

print("Music is playing in the background!")


bear = '''
           .=##*##=           -##*##=.           
          .#**####%###########%####**#.          
          -%*#==#%*************##==#*#=          
          .%*%+%*****************%+%*%.          
           .:*%*****+%****##%*****%#-.           
             -#*****@%*****@#*****#-             
             +#******%*%%%+%*******+             
             -#****#+=@@@@==+#****#-             
             .#****#====#====#****#.             
              .#***#+=++=**=+#***#.              
               .*#**#*######***#*.               
              .#****##%%%%##%****#.              
             .#**#*####%#%##%**#**#:             
            .%**#***##*****#****#**%.            
           .#**#*****************#**#.           
           :#**%*****************%**#-           
         =%###%@%***************%@%###%=.        
       .#*###***##*************##***###*#.       
       *#+====#****#*********#****#====+#*.      
       =%======%***#*********#***%======%+       
        #*=====%**#*+*********#**%=====*#.       
        .+*++=###=.           .=##%+++**.        
'''

ring = '''
                                                         
                                                         
                                                         
                                                         
                      .::.:::.:.:-.                      
                    :==----:::=+++==-                    
                   =+----:.....+++++=-                   
                    =++++---:::==:..:                    
                      =++-------::.                      
                       .++------..                       
                      ...:::::.....                      
                   .:.::........:::...                   
                 .......:......::....:..                 
                .:.....................:.                
              .:....:               .....:               
             .:...:.                 .:...:.             
             :...:.                   .:....             
             :....                     ....:             
            .:....                     ....:.            
            .:....                     ....:.            
             :....                     ....:             
             .:....                   ....:.             
              :.....                 .....:              
               .:.....             .....:.               
                .:.....................:.                
                  ...................:.                  
                    ..:.........:::..                    
                         .......                         
                                                         
                                                         
                                                         '''



# Game variables
turns = int(5)
points = int(0)


def check_game_status():
    global turns
    print("Turns left:", turns)
    if turns == 0 or points >= 5:
        conclusion()

def conclusion():
    print(("-") * 20)
    print(("-") * 20)
    print("It clicks, no wonder these clues were so familiar, you are the killer.")
    ascii_art = pyfiglet.figlet_format("You are your own enemy")
    print(ascii_art)
    print(("-") * 20)
    print(("-") * 20)

def room():

    def bed():
        global points
        global turns
        print("You duck down and search inside\n")
        for i in tqdm(range(101), desc="Searching…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("\nYou find a familiar looking teddy bear.\n")
        print(bear)
        print("Perhaps try searching the drawer")
        
        points += 1
        turns -= 1 
        check_game_status()
        print("Press Enter to return to the scene")
        start()

    def drawer():
        global room_finish 
        global points
        global turns
        print("You examine the drawer")
        for i in tqdm(range(101), desc="Searching…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("\nYou found a ring, it looks familiar...\n")
        print(ring)
        points += 1
        turns -= 1 
        print("Perhaps try searching under the bed")
        check_game_status() 
        room_finish = True

        start()
        check_game_status()  

    def start(): 
        print("\n", ("-") * 20)
        print("You have entered the room")
        print(("-") * 20)
        print("\n1: Check drawer")
        print("\n2. Look under bed")
        print("\n3. Exit room")
        selection = int(input("\nChoose option\n"))

        if selection == 1:
            if room_finish:
                print("You have already checked!")
            else:
                drawer()
        elif selection == 2:
            bed()
        elif selection == 3:
            initial()
        else:
            print("Invalid selection")
        print(("-") * 20)
    start()

def question():
    print("You approach the witness.")
    temper = random.choice(["aggressive", "scared"])
    print(f"The witness is {temper}. How do you want to question them?")
    print(("-") * 20)
    print("\n1: Calm them down ")
    print("\n2: Accuse them directly ")
    print("\n3: Walk away ")
    selection = int(input("\nChoose option\n"))
    print(("-") * 20)

    if selection == 1:
        global points
        global turns
        if temper == "scared":
    
            print("You calm them down, and they start talking.")
            print("They mention a struggle and someone familiar at the scene.")
            turns = turns -1 
            check_game_status()
        else:
            print("Your attempt to calm them fails. They grow agitated.")
            turns = turns -1 
            check_game_status()
        initial() 
        check_game_status() 

    elif selection == 2:
        print("You accuse them directly.")
        if temper == "aggressive":
            print("The witness lashes out. 'You're wasting time!'")
            turns -= 1 
            check_game_status()
            initial()
        else:
            print("The witness breaks down and cries, revealing partial information.")
            turns -= 1 
            check_game_status()
            initial()
    
 

    elif selection == 3:
        print("You walk away from the witness.")
        print("You need more clues to move forward.")
        input("Press Enter to continue...\n")
        initial() 
        check_game_status() 
    else:
        print("Invalid selection. Try again.")
        question()


def blood():
    print(("-") * 20)
    print("\n1: Examine")
    print("\n2. Leave")
    selection = int(input("\nChoose option\n"))
    print(("-") * 20)

    if selection == 1:
        print("You examine the blood")
        for i in tqdm(range(101), desc="Searching…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("The blood looks off, where have I seen it before?")
        blood()
    elif selection == 2:
        initial()
    else:
        print("Invalid selection")
    check_game_status()

def initial():
    global turns
    print(("-") * 20)
    print("\n1: Enter room")
    print("\n2: Question witness")
    print("\n3: Examine blood")
    selection = int(input("\nChoose option\n"))

    if selection == 1:
        room()
    elif selection == 2:
        question()
    elif selection == 3:
        blood()
    else:
        print("Invalid selection")

    turns -= 1  
    check_game_status()


ascii_art = pyfiglet.figlet_format("Welcome")
print(ascii_art)

print("You arrive at the murder scene in a bedroom. What do you do?")
print("You will have 5 turns to find which evil person did it.")
print("Navigate by entering numbers shown in menus")

initial()
