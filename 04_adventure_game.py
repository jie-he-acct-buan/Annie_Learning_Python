# introduction:
# I used python to write a text-based adventure game. 
# The game is like an interactive fiction.  
# In this game, user makes choice and moves through the story, 
# collecting items or answering questions.  

# Storyline: The user is hiking in a forest and hears a sound.
# She gets lost and has to make decisions so that
# she can get back safely and win the game.


# ===================================================================================
# chapter I: start of the story
# =====================================================================================
import time


hello = '''
Hi, welcome to puppy wonderland, at the planet pup.io!
You must go on an evening hike.
Good Luck!
'''
print(hello)
print('----------------------------------------------')
time.sleep(2)


q_tool = '''
You can pick one item to take with you!
What do you choose?
A. map
B. flashlight
C. dogbone
D. rope
E. hammer

ENTER A, B, C, D, E
''' 

ask = True
while ask:
    tool = input(q_tool).upper()
    if tool in ['A', 'B', 'C', 'D', 'E']:
        ask = False
print('----------------------------------------------')
time.sleep(2)


q_sound = ('''
You just heard a dog barking!
Do you want to follow the sound?         
A. Yes
B. No                  
What is your choice?      

ENTER A, B        
''')
ask = True
while ask:
    sound = input(q_sound).upper()
    if sound in ['A', 'B']:
        ask = False   
print('----------------------------------------------')
time.sleep(2)


if sound == 'A':
    print('''
You keep going toward the barking sound.
The sound suddenly stops.
You are now LOST!!!!
You try to call help but there is no signal!
''')
else:
    print('''
Good idea, you are not taking risks.
You start going back to the starting point.
But you realize that you are LOST!!!!

''')
print('----------------------------------------------')
time.sleep(2)



# ===================================================================================
# chapter II: Middle of nowhere
# =====================================================================================
q_direction = '''
Very unfotunaly, you got lost when you
pasted the ghost dog forest in the the past few hours,
So,now you have to guess direction for the path out of the hike.
A. east
B. south
C. west 
D. north
E. stay here

ENTER: A, B, C, D or E!

'''
ask = True
while ask:
    direction = input(q_direction).upper()
    if direction in ['A', 'B', 'C', 'D', 'E']:
        ask = False
print('-----------------------------------------------')
time.sleep(2)


if direction == 'A':
    print('You reach a cabin.')
    if tool == 'A':
        print('''
YAY! 
With the map in your bag,
You can find your way out of here!
YOU WIN!!
              ''')
    else:
        print('''
Without the map,
You can't find your way out of here!
YOU LOSE!!
              ''')

elif direction == 'B':
    print('''
You broke your leg from your 5 feet fall.
Sadly, you LOSE!!
''')

elif direction == 'C':
    print('''
Great!!
You found a bridge to cross the river to go outside!
BUT OMG...
It is broken.            
''')
    if tool == 'D':
        print('''
YAY! 
With the rope in your bag,
You can repair the bridge and get out of here!
YOU WIN!!
 ''')
    elif tool == 'E':
        print('''
YAY! 
With the hammer in your bag,
You can repair the bridge and get out of here!
YOU WIN!!
 ''')
    else:
        print('''
ON NO!
You picked neither rope nor hammer
Sadly, you can not fix the bridge.
You LOSE!!                            
''')        

elif direction == 'D':
    print('You reach a highway.')
    if tool == 'B':
        print('''
YAY! 
With the flashlight in your bag,
You can signal for help!
YOU WIN!! ''')
    else:
        print('''
OH NO!!! 
You wished you have picked the flashlight.
Without the flashlight, you can not signal for help.              
Sadly, you LOSE!!      
''')

else:
    q_corgi_1 = '''
You waited for 30 minutes.

Just when you were about to leave.
You saw a super cute corgi running towards you.

The super cute corgi said,
"arf! arf!
Hello!
My name is Buddy.
I am a magical dog.
I can grant a wish and become your pet!
What is your favorite programing language?"

'''
    corgi_1 = input(q_corgi_1).upper()
    time.sleep(2)

    if corgi_1 == 'PYTHON':
        print('''
-----------------------------------------------
"I totaly agree with you.
              
But (belly rumbles)              
I am sooooo hungrey.
              
(Go into begging postion)
Do you have a bone for me?
              
(look at you with adorable eyes)"
''')
        time.sleep(5)
        print('-----------------------------------------------')

        if tool == 'C':
            print('''
You found the bone in your bag.
Buddy was so happy.
                  
The puppy said, 
"Thank you!
(takes a bite out of the bone)
This bone is delicious! 
Now I can be your pet and show you the way out!"
                  
YOU TAMED BUDDY SO YOU WON!!!! 
 ''')
    
        else:
            print('''
You can not find anything to feed Buddy.
You wish you picked the dogbone.
Buddy is toooooo hungry to help you.
Sadly, you LOSE!!            
 ''')
    
    else:
        print('''
You are talking nonsense.
Python is the BEST programming language!
              
Learn this fun Python book,
then I will help you.

Sadly,you lose for now.
''' )            































