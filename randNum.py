from sys import exit
import random



#generates an integer between -9999999999999999999999999999999999999 and 9999999999999999999999999999999999999
def negPo():
    n1 = random.randint(-9999999999999999999999999999999999999,9999999999999999999999999999999999999)
    return n1

#generates a negative integer between -9999999999999999999999999999999999999 and -1
def neg():
    n2 = random.randint(-9999999999999999999999999999999999999,-1)
    return n2

#generates a positive integer between 0 and 9999999999999999999999999999999999999
def po():
    n3 = random.randint(0,9999999999999999999999999999999999999)
    return n3

#generates an integer between two numbers given by the user
def betw():
    n4 = 0
    x1 = 0
    x2 = 1000
    try:
        print("Choose a number: ")
        x1 = int(input())
        print("Choose another number: ")
        x2 = int(input())
        if x1 < x2:
            n4 = random.randint(x1,x2)
        elif x2 < x1:
            n4 = random.randint(x2,x1)
        elif x1 == x2:
            n4 = x1
    except ValueError as e:
        print("Incorrect format", e)
    return n4

#checks if user wants to quit or generate another number
def qc():
    ex = 0
    print("Do you want to quit?")
    inp = input()
    if inp == "yes" or inp == "yeh" or inp == "yep" or inp == "ye" or inp == "y":
        ex = 1
    return ex


#Gets the users choice on what kind of number he wants to generate
def menSel():
    choice = 1
    try:
        print("Input the number of your preferred option (Please choose an integer between 1 and 4 both included): ")
        choice = int(input())
    except ValueError as e:
        print("You did not choose a valid option. Please choose an integer between 1 and 4 both included.")
        choice = menSel()
    
    if choice < 1 and choice > 4:
            print("You did not choose a valid option. Please choose an integer between 1 and 4 both included.")
            choice = menSel()
        
    return choice


#main part of the program that calls out to the other funcions
def main():
    #First message shown which includes a menu showing the options%
    print("Welcome to the Random Number Generator\n What kind of number do you want to generate?: \n 1-Negative and Positive\n 2-Negative only\n 3-Positive only\n 4-Between two inputed numbers")

    #Calls a function to get which menu option the user wants
    rnd = menSel()
    if rnd == 1:
        #calls the function that generates a random integer that could be possitive or negative
        a = negPo()
        print("The random generated number is: \n", a)
    elif rnd == 2:
        #calls the function that generates a random negative integer
        a = neg()
        print("The random generated number is: \n", a)
    elif rnd == 3:
        #calls the function that generates a random positive integer
        a = po()
        print("The random generated number is: \n", a)
    elif rnd == 4:
        #calls the function that generates a random integer between two numbers inputed by the user
        a = betw()
        print("The random generated number is: \n", a)
    else:
        print("You did not choose a valid option. Please choose an integer between 1 and 4 both included.")
        main()
    
    
    #calls the function that chacks if the user wants to quit
    q=qc()
    if q == 1:
        print("Bye")
        #exits the program
        exit()
    else:
        #reloads the program
        main()
    

main()