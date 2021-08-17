def count_iterative(string):
    count=0
    for c in string:
     if c.isspace()!=True:
        count += 1
    return count

def count_recursive(string):
    if not string:
        return 0
    else:
        
         return 1 + count_recursive(string[1:])

def main():
    string = input("Please enter a string: ")
    print(count_iterative(string))
    print(count_recursive(string))

main()
