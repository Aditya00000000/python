def power(n, e):
    if e == 0:
        return 1
    elif e == 1:
        return n
    else:
        return (n*power(n, e-1))
n = int(input("Enter the base: "))
p = int(input("Enter the power: "))
b=power(n, p)
print("the exponent value of ",n," and ",p,"is : ", b)