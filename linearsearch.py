def linearsearch(a,n,val):
    for i in range(0,n):
        if(a[i]==val):
            return i+1
    return -1
n=int(input("Enter the number of elements to be entered: "))
print("Enter the elements in the array: ")
a=[int(input()) for i in range(n)]
val=int(input("Enter the value to be searched: "))
res=linearsearch(a,n,val)
if (res==-1):
    print("THE VALUE SEARCHED IS NOT PRESENT IN THE LIST....")
else:
    print("ENTERED VALUE IS PRESENT AT ",res)