import pyfiglet
import random
from pygame.base import init
from tqdm import tqdm
import time
from pydub import AudioSegment
from pydub.playback import play
import pygame
import sys

# Initialize pygame mixer
pygame.mixer.init()

# Load the .wav file
pygame.mixer.music.load("song.wav")

# Play the music
pygame.mixer.music.play(-1) 

print("Music is playing in the background!")

shelf = '''
                                                         
                                                         
                                                         
         .......................................         
      :*===------::::::------:::----:::::-======+*:      
    :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%-    
    :#####################################*########%:    
     -#*#######*#####**##########################%%=     
      ==********************#**********************      
      ===:::::::::::--=====+%=--:---============+*+      
      ===::::-##****##*:::-+%=::::-##****###:--=+#+      
      ===:-::-*+*###*+=::---%=:::::*+*###*+=::-:=*+      
      ===::::::::::::::::::-%=::::::::::::::::::-#+      
      ==%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%*+      
      ====+++++++++++++++++++++++++++++++++++++++*+      
      ===:---::::::::::::::::::::::::---========+*+      
      ===:::::::::::::::%=..:-=+%-::::::::-:::--+*+      
      ===:::::::::::::::-:-----:-:::::::::::::::=*+      
      =+=::-----------------------------------:-=#+      
      =-++***************************************++      
      ===--=====================================+*+      
      ===:::::::::::::::-:-::-:-:-:::::-----====+*+      
      ===:-::::::::::::-*=...:==*-::::::::::::-:=*+      
      ===::::::::::::-:-:-:::::-::::::::::::::::=*+      
      ===::::--::----:::::::::::::----::::--::::=#+      
      =:----------------------------=+++=======++=+      
      .=-=+%-                               -#-==*.      
                                                         
                                                         
                                                         
                                                         
                ..   .  .        - .:=:.:-:..            
               ....   . .. ...   ..     .....            '''

bed_img = '''
                                 :--====--:.             
                          ==+--=+=+++++++===+=-          
                         .*+**+++*+======+++++==+.       
                         .@*#+==*  .....-+*+==++=++.     
                          +++=*:            :+****=+*=== 
                          :+++:                ++=+**+++ 
   :                    .+@+-*:             .==*+==*#+*+ 
 +====             .-*:     .--.           .+-=++==+***= 
 =+**-    .....:*#*******#+:.   =+:..      -==#*++++**#= 
 :*+#++*=========*#***********#*-:. .-====:.-+=-:-=*#*#- 
 .***==++++***+*++===****************=::   .. .*+==+**#: 
 .#*#+============+++==+##***+*#********#++-::.*===+**%: 
 .#+*================++==+%%===%*******#####...*===+**%. 
 .#+*==================+*==*##******##%#####...*===+**%. 
 .#+*====================++**+**#%#########*...+==****%. 
  *+*=====================+@#**############*...+-.  :+-  
  *+#+=====================##**############*.:+=         
  *+*- -*#+================##**###########%*.            
   :.       -#*============##**########%=                
                 +*+=======##**######:                   
                     :++=+=##**###:                      
                         .=%#**:                         
                           -#**.               ..........
                            -++.              =**########'''

blood_img = '''


                        ..                 
                       =##:                
               ==.     *##.                
              :##+    .##*                 
              .%#+    -##:                 
         +*.   *#*   .*#*  :.              
         =%#   +###++####+###:.            
          .%#-=%###########=+#*            
           =####%%############- .-=-       
   .-:..  :%######%################=       
  .+#*****%%########%###########=:.        
           #%%########%########:           
           #%%%########%%######*=--:       
         .+%%%%%%########%%####+++*=.      
      .-*%*+*%%%%%%%#####*=*%#.            
     :#%*.   -%%*-:.-*%%:   =#.            
      ..     +#.     :#*.   :%*            
            *#       =%*.    :.            
          .#%:      .*%=                   
          #%+        ..                    
          :.                               

                                           '''

detective = '''
                                   -@@=.+@@-                                     
                                   @@@@@@@@@                                     
                                  +@@@@@@@@@+                                    
                                  *@@@@@@@@@@:.                                  
                             @@@@@@@@@@@@@@@@@@@@:                               
                                  @@@@@@@@@@@                                    
                                  =@@@@@@@@@.                                    
                                   #@@@@@@@*                                     
                                 %@@@@@@@@@=@@.                                  
                              .@@@@#+@@@@@@.@@@@@                                
                             @@@@@@   @@@%  @@@%                                 
                             :=*@@@   @#%. @@@@@@@@@@@#                          
                       :@@@@@@@@@@#    @% *@@@@@@@@@@@@:                         
                       =@@@@@@@@@@@   :@* =@@@@@@@@@@@@@                         
                       #@@@@@@@@@@@.  +@@ @@@@@@@@@@@@@@-                        
                       @@@@@@@@@@@@-@.#@@%@@@@@@@@@@@@@@@+                       
                       =@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@-                       
                       @@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@%                       
                      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                       
                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                     
                     %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@@@.                    
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ -@@@@@@.                    
                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ +@@@@@+                     
                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@-  #@@@@@                     
                      +@@@@@@@@@@@@@@@@@@@@@@@@@@@@  :@@@@@%                     
                      =@@@@@@@@@@@@@@@@@@@@@@@@@@@@# %@@@@@                      
                      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                      
                       -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                        '''

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
    print("You have", turns, "turns to find the killer")
    if turns == 0 or points >= 5:
        conclusion()

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def conclusion():
    print("\n", "-" * 40)
    print("-" * 40)
    type_effect("The pieces fall into place...", 0.05)
    type_effect("A chilling realization dawns upon you.", 0.05)
    type_effect("The clues lead back to someone...", 0.05)
    type_effect("You are the killer.", 0.1) 
    print("-" * 40)
    ascii_art = pyfiglet.figlet_format("You are your own enemy", font="slant")
    print(ascii_art)
    print("-" * 40)
    quit()

def room():

    def bed():
        global points
        global turns
        print(bed_img)
        print("You duck down and search inside\n")
        for i in tqdm(range(200), desc="Searching…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("\nYou find a familiar looking teddy bear.\n")
        print(bear)
        print("Perhaps try searching the drawer or questioning a witness")
        
        points += 1
        turns -= 1 
        check_game_status()
        print("Press Enter to return to the scene")
        start()

    def drawer():
        global points
        global turns
        print(shelf)
        print("You examine the drawer")
        for i in tqdm(range(200), desc="Searching…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("\nYou found a ring, it looks familiar...\n")
        print(ring)
        points += 1
        turns -= 1 
        print("Perhaps try searching under the bed or questioning a witness")
        check_game_status() 

        start()
        check_game_status()  

    def start(): 
        print(("-") * 20)
        print("You have entered the room")
        print(("-") * 20)
        print("\n1: Check drawer")
        print("\n2. Look under bed")
        print("\n3. Exit room")
        selection = int(input("\nChoose option\n"))

        if selection == 1:
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
    print(blood_img)
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
print(detective)

print("\nDetective, You arrive at the murder scene in a bedroom. What do you do?")
print("You have 5 turns to unravell this mystery.")
print("Use numbers to progress through the story, pay close attention to every detail.")
print("Hurry up, The truth awaits and time is running out!")

initial()
