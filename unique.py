import sys
try:
    string = sys.arv[1]
except:
    print("python unique.py \"Any string you want\"")
else:
    boolean = True
    for x in string:
        count = 0
        for y in string:
            if x==y:
                count += 1
            if count > 1:
                boolean = False
            print(x, " : ", count)
        if boolean:
            print("Unique! All characters appear only once.")
        else:
            print("Not unique! One or more characters appear more than once.")
