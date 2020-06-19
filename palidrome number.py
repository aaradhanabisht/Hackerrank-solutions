## palindrome number

n = int(input("Enter a number"))
rev = 0
x = n
while(x>0):
    rev = rev * 10
    rev = rev + (x%10)
    x = x//10
print(rev)
if(n==rev):
    print(n," is a palindrome number")
else:
    print(n," is not a palindrome number")
