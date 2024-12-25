import time




# chatbot gives the greeting
greeting = '''
Hello, I am "Corgi Arf01".
OOPS, I meant "Corgi 101". I am a chatbot.
I like animals and I love to talk about food!
'''
print(greeting)
time.sleep(2)


# chatbot asks name
name = input('What is your name? ')
print('Hello {}, nice to meet you!'.format(name))
print()
time.sleep(2)


# chatbot asks year
year = int(input('What is the year? '))
print("That's correct. Thank you!")
print()
time.sleep(2)


# chatbot asks age of chatbot
age = int(input('Can you guess my age? ' ))
print('Yes you are right. I am {} years old.'.format(age))
time.sleep(2)


future = 100 - age
print('I will be 100 in {} years.'.format(future))
time.sleep(2)


future_year = year + future
print('That will be the year {}.'.format(future_year))
print()
time.sleep(2)


# chatbot asks favorite food
food = input('What is your favorite food? ')
print('I like {} too!'.format(food))
print()
time.sleep(2)


input('How often do you eat {}? '.format(food))
print('Same as me, my owner gives me {} for my dishes too!'.format(food))
print()
time.sleep(2)


# Chatbot asks favorite animals
animal = input('My favorite animal is cats. What is yours? ')
print('I like {} too!'.format(animal))
print('I wonder if {} like to eat {} too!'.format(animal, food))
print()
time.sleep(2)


# Chatbot asks feeling today and reason for feeling
feeling = input('How are you feeling today? ')
print()
input('Why are you feeling {} today? Can you please tell me? '.format(feeling))
time.sleep(2)


# Chatbot says Goodbye
goodbye_1 =  '''
I understand. Thanks for sharing.
'''

goodbye_2 = '''
......
Oh no! M_y ba_tt_ery i_s l_ow!
......
'''

goodbye_3 = '''
My owner is calling me for charging my battery.
We can chat again later.
Goodbye {} I liked chatting with you!
Woof!Woof!
'''

print(goodbye_1)
time.sleep(4)


print(goodbye_2)
time.sleep(4)


print(goodbye_3.format(name))









