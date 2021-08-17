try:
 enterfile = input("Enter the file name: ")
 file = open(enterfile, 'r')
 linecount = 0
except FileNotFoundError:
    print("I cannot open the file", enterfile,"- Please check the name and try again.")
for line in file:
    linecount = linecount + 1

print("The number of lines in this txt. file is", linecount)

while True:
    try:
     linenum = 0

     num = int(input("Please enter a line number or press 0 to quit: "))
     if num < 1:
        print("Try again. Line number must be between 0 and", linecount)
     if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    except ValueError:
        
         print("Try again. Line number must be between 0 and", linecount)
           
    else:
         if num == 0:
            
   
    break
