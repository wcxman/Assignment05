class BasicMathOperations():
    #NOTE: For all methods, unless otherwise noted, all parameters should be floats or integers.
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
    def factorial(self,num): #Calculates the factorial of an INTEGER using recursion
        if type(num) is int and num >= 0: #Making sure that the given number is a integer greater than or equal to zero
            if num == 0 or num == 1: #If the given number is zero or one
                return(1) #Returns 1
            else:
                return(num*self.factorial(num-1)) #Returns the current number times the factorial of the number smaller than it
        else:
            print("Error: num must be zero or a positive integer")
    def counting(self,start,end): #A method for printing a comma seperated output with each integer between and including the start and end parameters, as INTEGERS
        if type(start) is int and type(end) is int: #If both numbers are integers
            if end > start: #If the ending number is greater than the starting number
                for i in range (start,end): #For each number between start and end, inclusive
                    print(str(i) + ", ", end="") #Prints out the current iteration of the loop and a comma with a space, not breaking lines between
                print(end) #Prints out the last number of the sequence without a comma and with a line break
            else:
                print("Error: end must be greater than start.")
        else:
            print("Error: start and end must both be integers")
    def calculateHypotenuse(self,a,b): #A method to calculate the hypoteneuse of a right triangle from the two other sides. Note the method does not check if the numbers are both positive, as this can be useful for graphing applications. 
        if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float): #If both numbers are numbers
            return (self.calculateSquare(a)+self.calculateSquare(b))**0.5 #Returns the square root of the sum of a squared and b squared, which is the Pythagorean theorem.
        else:
            print("Error: a and b must both be numbers")
    def areaRect(self,l,h): #A method to calculate the area of a rectangle given length l and width w
        if (type(l) is int or type(l) is float) and (type(h) is int or type(h) is float): #Making sure the numbers given are numbers
            return l*h #Returns length times height
        else:
            print("Error: l and h must both be numbers.")
    def numPow(self,n,power): #A method to calculate a number n to a power
        if(type(n) is int or type(n) is float) and (type(power) is int or type(power) is float): #Making sure the numbers given are numbers
            return n**power #Returns n to the given power
        else:
            print("Error: n and power must both be numbers.")
    def argumentType(self,arg): #A method to return the type of an argument "arg"
        return type(arg) #Returns the type of arg
def main():
    a = BasicMathOperations()
    todo = True
    print('''Welcome to the math operations interface! Commands:
              GREET: Greets you, the user
              ADD: Adds two numbers
              OP: Takes two numbers and uses the specified operation on them
              SQ: Squares a number
              FAC: Takes the factorial of a number
              COUNT: Counts between two integers
              HYP: Calculates the hypotenuse of a right triangle given base and height
              RECT: Calculates the area of a rectangle given length and height
              POW: Takes a number to a power
              TYPE: Shows the type of an argument
              EXIT: Exits the interface''') #Sets up the user interface
    while(todo): #Repeats until the user exits
        cmd = str(input("")).upper() #Takes the user's command and sets it to all uppercase
        if cmd == "EXIT":
            todo = False #Breaks the while loop
        elif cmd == "GREET":
            a.greet()
        elif cmd == "ADD":
            a.add() #Uses the add method
        elif cmd == "OP":
            n1 = float(input("First number? ")) #Takes the user's values
            n2 = float(input("Second number? "))
            op = input("Operation character? ")
            if a.operation(n1, n2, op) is not None: #If the operation does not return any errors
                print(str(n1) + op + str(n2), "=", a.operation(n1, n2, op)) #Prints out the result
        elif cmd == "SQ":
            n1 = float(input("Number: ")) #Takes the user's value
            print(str(n1) + "^2" , "=", a.calculateSquare(n1)) #Prints out the result
        elif cmd == "FAC":
            n1 = int(input("Integer: ")) #Takes the user's value
            if a.factorial(n1) is not None: #If the method will return a value (if it doesn't, the error message is baked into the method)
                print(str(n1) + "!" , "=", a.factorial(n1))
        elif cmd == "COUNT":
            start = int(input("Start (integer): ")) #Takes the user's values
            end = int(input("End (integer): "))
            a.counting(start, end) #Uses the counting method, which prints itself without returning anything\
        elif cmd == "HYP":
            aa = float(input("a: ")) #Takes the values
            b = float(input("b: "))
            print(str(aa) + "^2", "+", str(b) + "^2", "=", a.calculateHypotenuse(aa,b)**2) #Shows the answer in equation form
            print("c", "=", a.calculateHypotenuse(aa, b)) #Shows the real value for c
        elif cmd == "RECT": 
            l = float(input("Length: "))
            h = float(input("Height: "))
            print("The area of the rectange is", a.areaRect(l, h))
        elif cmd == "POW":
            num = float(input("Number to be raised: "))
            power = float(input("Power: "))
            print(str(num) + "^" + str(power), "=", a.numPow(num, power))
        elif cmd == "TYPE":
            inp = input("Argument: ")
            print(a.argumentType(inp))
        else:
            print("Error: Unrecognized Command")
main()
