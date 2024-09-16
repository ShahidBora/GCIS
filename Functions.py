
#Below is carry over functions
def Add():
    a = 5
    return(5+a)

def Multi():
    MultiAdd = Add()
    return(5 * MultiAdd)

def Div():
    MultiAddDiv = Multi()
    return (MultiAddDiv/2)

def main():
    print(Div())
main()

#Below is input once and call 3 functions

def addition(x,y):
    return (x+y)
def div(x,y):
    return(x/y)
def multiply(x,y):
    return (x*y)

def main():
    x = int(input("First number:"))
    y = int(input("Second number:"))
    print (addition(x,y))
    print (div(x,y))
    print (multiply(x,y))

main()
