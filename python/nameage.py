import time
start_time = time.time()

print('What is your name?')

myName = input()

while myName != 'daniel':
    if myName == 'your name':
        print('Ha ha, very funny.  Who are you?')
        
        myName = input()
    else:
        print('That is not your name.  Please, tell me your real name')
        myName = input()

print("Hello, " + myName + ". That is a good name.  How old are you?")

myAge = input()

if int(myAge) < 13:
    print("Learning young, that's good")

elif int(myAge) == 13:
    print("You're a teenager now... that's cool I guess")

elif int(myAge) > 13 and int(myAge) < 30:
    print("Still young, still learning")

elif int(myAge) >= 30 and int(myAge) < 65:
    print("now you're adulting")

else:

    print("... you've lived a long time?")
    

















#programAge = int(time.time() - start_time)

#print(myAge + "? That's funny, I'm only " + str(programAge) + " second old")

#time.sleep(3)

#print("I'm tired. I go sleep now.")



