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
        if type(num1) is float or type(num1) is int: #Checking both num1 and num2 are numbers
            if type(num2) is float or type(num2) is int:
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
    def calculateSquare(self,num): #Calculates the square of the number given by the user
        if type(num) is float or type(num) is int: #Making sure the given number is actually a number
            return(num*num)
        else:
            print("Error: num must be a number")
    def factorial(self,num): #Calculates the factorial of an integer using recursion because it's a free country
        if type(num) is int and num >= 0: #Making sure that the given number is a integer greater than or equal to zero
            if num == 0 or num == 1: #If the given number is zero or one
                return(1) #Returns 1
            else:
                return(num*self.factorial(num-1)) #Returns the current number times the factorial of the number smaller than it
        else:
            print("Error: num must be zero or a positive integer")
    
def main():
    a = BasicMathOperations()
    print(a.calculateSquare(10))
    print(a.calculateSquare("elf"))
    print(a.factorial(10))
    print(a.factorial(-1))  
    print(a.factorial("dog"))
    
main()
