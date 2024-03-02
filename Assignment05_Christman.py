class BasicMathOperations():
    def greet(self): #Creates a method for greeting the user
        fn = str(input("First Name? ")) #Collecting the user's first name
        ln = str(input("Last Name? ")) #Collecting the user's last name
        print("Hello", fn, ln + "!") #Greeting them
    def add(self): #Creates a method to add two user-provided numbers
        num1 = float(input("First number? ")) #Collecting the user's first number
        num2 = float(input("Second number? ")) #Collecting the user's second number
        print(str(num1) + "+" + str(num2), "=", num1+num2) #Returning the sum of those two numbers to the terminal
        return num1+num2 #Actually returning the sum
    def operation(self,num1,num2,operator): #Creates a method to do a certain operator on two numbers. Valid operator calls: addition - "+", subtraction - "-", multiplication "*" or "x", division "/". 
        if type(num1) == float or type(num1) == int: #Checking both num1 and num2 are numbers
            if type(num2) == float or type(num2) == int:
                if operator == "+": #If the operator is addition
                    return num1+num2 #Returns the sum of the numbers
                elif operator == "-": #If the operator is subtraction
                    return num1-num2 #Returns the difference of the numbers
                elif operator == "*" or operator == "x": #If the operator is multiplication
                    return num1*num2 #Returns the two multiplied
                elif operator == "/": #If the operator is division
                    return num1/num2 #Returns the two divided
                else:
                    print("Error: Unknown operator") #If the operator doesn't have a defined function
            else:
                print("Error: num1 and num2 must be float or integer values") #Error for if user puts non-numbers into the function
        else:
            print("Error: num1 and num2 must be float or integer values") #Error for if user puts non-numbers into the function

def main():
    obj1 = BasicMathOperations()
    print(obj1.operation(12,4,"/"))
    print(obj1.operation(15,8,"*"))
    print(obj1.operation(12,5,"-"))
    print(obj1.operation(15,2,"+"))
    print(obj1.operation("Snail",2,"+"))
    print(obj1.operation(1,2,"Snail"))
    print(obj1.operation(1,"Snail",2))
    print(type(obj1))
    
main()
