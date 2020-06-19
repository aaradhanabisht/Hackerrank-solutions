i=1
j=1
n=int(input("enter length"))
m=n
a=n
while m>=0:
    while i<=n:
        print(" "*m,"* "*i)
        m=m-1
        i=i+1
    while j<=a:
        print(" "*j,"* "*n)
        n=n-1
        j=j+1
