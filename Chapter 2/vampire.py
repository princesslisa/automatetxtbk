name = input("What is your name? ")
age = int(input("\nHow old are you? "))

if name == 'Alice':
 print('Hi, Alice.')
elif age < 12:
 print('You are not Alice, kiddo.')
elif age > 2000:
 print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
 print('You are not Alice, grannie.')