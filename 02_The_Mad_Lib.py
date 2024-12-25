import time

# self introduction
hello = '''
Hi, I am a robot telling jokes.
Could you please answer several questions?
'''
print(hello)
print()
time.sleep(1)

# =======================================================================
#  joke 1
# =======================================================================

# Name your favorite food
food = input('What is your favorite food? ')
print()
time.sleep(1)


# Name a resturant
place = input('What is your favorite resturant? ') 
print()
time.sleep(1)


# Name a color
color = input('What is your favorite color? ')
print()
time.sleep(1)


# Name an person
person = input('Who is the person you are thinking about now? ')
print()
time.sleep(1)


# Name an animal
animal = input('Can you name a cute animal? ')
print()
time.sleep(1)


# Name a verb
verb = input('What is your least favorite thing to do? ')
print()
time.sleep(1)


say_1 = '''
I just made a joke for you:
===================================================================
{} went into {} to order a {}. 
BUT, {} did not have enough money.
The boss said, 
"I can offer you a free {} 
IF you {} with a {} {}."
===================================================================
'''
print(say_1.format(person, place, food, person, food, verb, color, animal))
print()
time.sleep(5)


# =======================================================================
#  joke 2
# =======================================================================


# Robot asks more questions
print('''
I have another joke for you. 
But first, let us answer more questions!
''')
print()
time.sleep(1)


# Name a Icecream flavor
flavor = input('Can you name a Icecream flavor? ')
print()
time.sleep(1)


# Name a type of exercise
stay_fit = input('Can you name a type of exercise that you enjoy doing to stay fit? ')
print()
time.sleep(1)


# Name a thing that is a animal or human
name = input('Can you tell me a funny name? ') 
print()
time.sleep(1)


#  Name a place you like to shop
shopping = input('Can you name a place you like to shop? ')
print()
time.sleep(1)


#  Name a funny animal
funny_animal = input('Can you name a funny animal? ')
print()
time.sleep(1)


say_2 = '''
Here is another very funny joke:
===================================================================
{} went into {} to eat a {} flavored ice cream.
BUT, there was a funny event today at {}, and it was:
{} with a {}!  
===================================================================
'''
print(say_2. format(name, shopping, flavor, shopping, stay_fit, funny_animal))




