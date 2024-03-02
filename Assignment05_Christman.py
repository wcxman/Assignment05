class BasicMathOperations():
    def greet(self):
        fn = str(input("First Name? "))
        ln = str(input("Last Name? "))
        print("Hello", fn, ln + "!")

def main():
    obj1 = BasicMathOperations()
    obj1.greet()
    
main()