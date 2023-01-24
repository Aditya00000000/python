import numpy as np

def mul(r1,r2,c1,c2,a,b):
    m=r1
    n=c1
    result=[[0 for i in range(n)]for i in range(m)]
    if(r1==c2 or c1==r2):
        result = np.dot(a,b)
    else:
        print("TWO ARRAYS HAVE DIFFERENT NUMBER OF ROWS AND COLUMNS: ")

    print("MULTIPLICATION OF THE TWO MATRIX IS: ")
    for i in range(m):
        for j in range (n):
            print(result[i][j],end =" ")
        print()


def arrayprint(r,c,mat):
    for i in range(r):
        for j in range (c):
            print(a[i][j],end =" ")
        print()


#FIRST ARRAY....


print("ENTER THE DATA FOR THE FIRST MATRIX: ")
r1=int(input("ENTER THE NUMBER OF ROWS: "))
c1=int(input("ENTER THE NUMBER OF COLUMNS: "))
print("ENTER THE ELEMENTS IN THE 1ST MATRIX: ")
a=[[int(input())for i in range(c1)]for i in range (r1)]
print("FIRST ARRAY IS: ")
arrayprint(r1,c1,a)


#SECOND ARRAY....


print("ENTER THE DATA FOR THE SECOND MATRIX: ")
r2=int(input("ENTER THE NUMBER OF ROWS: "))
c2=int(input("ENTER THE NUMBER OF COLUMNS: "))
print("ENTER THE ELEMENTS IN THE 2ND MATRIX: ")
b=[[int(input())for i in range(c2)]for i in range (r2)]
print("SECOND ARRAY IS: ")
arrayprint(r2,c2,b)


mul(r1,r2,c1,c2,a,b)


