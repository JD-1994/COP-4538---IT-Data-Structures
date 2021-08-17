#Joshua Diaz
#numberguess.py
#January 19, 2020
import random
def main() :
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    print("Think of a number between", smaller, "and" , larger)
    count = 1
    
    while True:
        print("I know your number is between ", smaller, "and", larger)
        guess = smaller + ((larger-smaller)//2)
        print("Is your number ", guess,"?")
        userRespond = input("Enter either = < or >: ") 
        if userRespond == "<":
            larger = guess
            count += 1

        elif userRespond == ">":
            smaller = guess
            count += 1
            
        elif userRespond == "=":
            print("I win! I guess about", count, "tries!")
            break
        else:
            print("Please enter a valid response")
main() 
