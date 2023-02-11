from art import logo

#add
def add (n1,n2):
    return n1+n2
#subtract
def sub (n1,n2):
    return n1-n2
#multiply
def mult (n1,n2):
    return n1*n2
#divide
def div (n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div,
}

print(logo)

def calculator():
    num1=int(input("First number: "))
    for op in operations:
        print(op)
    exit=False

    while not exit:
        symbol=input("Select an operation: ")
        num2=int(input("Next number: "))
        answer=operations[symbol](num1,num2)

        print(f"{num1} {symbol} {num2} = {answer}")
        stay=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if stay=="y":
            exit=False
            num1=answer
        else:
            exit=True
            calculator()
            
calculator()

    # symbol=input("Select another operation: ")
    # num3=int(input("Next number: "))
    # second_answer=operations[symbol](answer,num3)

    # print(f"{answer} {symbol} {num3} = {second_answer}")