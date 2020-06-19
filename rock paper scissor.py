##rock,paper,scissor

rock="r"
paper="p"
scissor="s"

p1=input("Player1 Enter your choice : ")
p2=input("Player2 Enter you choice : ")

def game():
    if(p1==p2):
        print("Its a TIE!!")
    elif(p1=="r" and p2=="p"):
        print("Player 2 wins")
    elif(p1=="r" and p2=="s"):
        print("Player 1 wins")
    elif(p1=="p" and p2=="s"):
        print("Player 2 wins")
    elif(p1=="p" and p2=="r"):
        print("Player 1 wins")
    elif(p1=="s" and p2=="r"):
        print("Player 2 wins")
    elif(p1=="s" and p2=="p"):
        print("Player 1 wins")
    else:
        print("Enter a valid input")
         
game()
