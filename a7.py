"""
File: a7.py

"""

from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() # Creates a stack called stk.

    # *** Write your code here ***
    for i in sentence:
        stk.push(i)
    #create another empty stack
        stk2=Stack()
    #poping out element from stk and pushing into stack stk2
        while stk.size():
            stk2.push(stk.pop())
    #since stk is empty, inserting the character into 'stk'
        for i in sentence:
            stk.push(i)
    #checking character equality in both stacks
        if stk2.size() and stk.size():
            if stk.pop == stk2.pop():
                pass
            else:
                return False
    return True

# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
