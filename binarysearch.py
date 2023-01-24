def binarysearch(a,beg,end,val):
    if (end>beg):
        mid=int((beg+end)/2)
        if(a[mid]==val):
            return mid+1
        elif(a[mid]>val):
            return binarysearch(a,0,mid-1,val)
        else:
            return binarysearch(a,mid+1,n,val)
    return -1
n=int(input("Enter the number of elements to be entered: "))
print("Enter the elements in the array in sorted order: ")
a=[int(input()) for i in range(n)]
val=int(input("Enter the value to be searched: "))
res=binarysearch(a,0,n,val)
if (res==-1):
    print("THE VALUE SEARCHED IS NOT PRESENT IN THE LIST....")
else:
    print("ENTERED VALUE IS PRESENT AT ",res)