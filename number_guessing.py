#To generate a random number we will use the module named random.
#In order to use this module we need to first import it.
import random

#Now we can use it to set our generated number between two set values. 
# Ex. (1, 10)
number = random.randint(1, 666)

#We can make this look better by asking for user feedback like name.
#(OPTIONAL) unless you have multiplayer enabled.
player_name = input("Hello player, What should I call you? ")

#Variables
number_of_guesses = 0

#Now since we are going with the optional piece aswell, we might aswell have fun!. 

#Ill write down the other formate below.
#If you don't need player_name then code string would be...
#print('I am guessing of a number between 1 and 666:')

#Now since we will incorperate a player name we will make him fight a evil monster.
#Which we will have as the computer as our villian.
print('Finally! '+ player_name+ ' I been waiting for a mortal to guess my number between 1 and 666 for thousands of years. What will your number be? :')

#Now we need to create our loop to keep guessing the number to beat this monster!
while number_of_guesses < 5:
    guess= int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too Low mortal, Try again!!!!!!!')
    if guess > number:
        print('Your number is too high you fool, Try again!')
    if guess == number:
        break

    if guess == number:
        print('Oh  Nooooooooo, You guessed the number of' + str(number) + 'and defeated me in only ' + str(number_of_guesses) + 'tries')
    
    else:
#here we can add + str(number to display what number the computer was thinking of)
        print('You cannot defeat the all powerful, maybe next time you might guess it! ')
