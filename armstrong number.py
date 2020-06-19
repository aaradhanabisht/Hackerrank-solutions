#armstrong number

n = int(input("Enter a 3 digit number "))
res = 0
x = n
while(x>0):
    rem = x%10
    res = (rem*rem*rem) + res
    x = x//10
if(n==res):
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")
