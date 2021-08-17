def magic_sequential(l):
    for i in range(len(l)):
        if(l[i]==i):
            return i
    return -1

def magic_binary(l):
    start = 0
    end = len(l)-1
  
    while(start<end):
        mid = int((start+end)/2)
        if(l[mid]==mid):
            return mid
        elif(l[mid]>mid):
            end = mid
        else:
            start = mid+1
    return -1

def main():
    n= int(input("Enter the number of integers to be entered in ascending order: "))
    l=[]
    while(n>0):
        k = int(input("Enter number: "))
        l.append(k)
        n = n-1
  
    print(magic_sequential(l))
    print(magic_binary(l))
  
main()
