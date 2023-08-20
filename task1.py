#SIMPLE CALCULATOR
def addnumbers(x, y):
    return x + y


def subtractnumbers(x, y):
    return x - y


def multiplynumbers(x, y):
    return x * y


def dividenumbers(x, y):
    return x / y

print("-----*****THIS IS A CALCULATOR THAT PERFORM SOME BASIC ARITHMETIC OPERATIONS *****-----")
print("Select operation you need to perform.")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")


while True:
    
    op = input("Enter choice(a/b/c/d): ")


    if op in ('a', 'b', 'c', 'd'):
        try:
            number1 = float(input("Enter first no.: "))
            number2 = float(input("Enter second no.: "))
        except ValueError:
            print("Invalid input entered.")
            continue

        if op == 'a':
            print("ADDITION OF NUMBERS IS:",number1, "+", number2, "=", addnumbers(number1, number2))
            

        elif op == 'b':
            print("SUBTRACTION OF NUMBERS IS:",number1, "-", number2, "=", subtractnumbers(number1, number2))
            

        elif op == 'c':
            print("MULTIPLICATION OF NUMBERS IS:",number1, "*", number2, "=", multiplynumbers(number1, number2))
          

        elif op == 'd':
            print("DIVISION OF NUMBERS IS:",number1, "/", number2, "=", dividenumbers(number1, number2))
     
       
        
        
        c = input("do you want to carry out more calculations ? (yes/no): ")
        if c == "no":
          break
    else:
        print("Invalid Input")
