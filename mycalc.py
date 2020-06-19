import re

print("My Calculator")
print("Type 'quit' to end")
previous = 0
run = True

def performMath():
    global previous
    global run
    equation = ""
    
    if(previous == 0):
        equation = input("Enter equation : ")
    else:
        equation = input(str(previous))
        
    if(equation == 'quit'):
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[A-za-z,.\"\':()" "]','',equation)
        if(previous == 0):
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()
