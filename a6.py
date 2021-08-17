"""
File: a6.py
Assignment 6

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    
    # ADD CODE HERE: Count the number of nodes in the structure
    while probe != None:
        count +=1
        probe = probe.next
    return count
    
def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    if head == None:
       head =Node(newItem)       
    else:
        prev = None
        curr = head
        while curr != None:
            if newItem < curr.data:
                break
            prev = curr
            curr = curr.next

        n = Node(newItem, curr)
        if prev == None:
            head = n
        else:
            prev.next = n
        
    return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    # ADD CODE HERE
    probe = head
    while probe != None:
        print(probe.data, end=' ')
        probe = probe.next
    print()
def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    
    head = None
    userInput = input('Please enter a word (or just hit enter to end): ')
    while userInput != '':
        head = insert(userInput, head)
        userInput = input('Please enter a word (or just hit enter to end): ')
    print('The structure contains', length(head), 'items:')
    printStructure(head)

if __name__ == "__main__": main()
