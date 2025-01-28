class calculator:
    def __init__(self):
        self.num1 = int(input("Enter number: "))
        self.num2 = int(input("Enter number: "))

    def add(self):
        r = self.num1 + self.num2
        return f"the sum of {str(self.num1)} and {str(self.num2)} is {str(r)}"
    
    def sub(self):
        r = self.num1 - self.num2
        return f"the subraction of {str(self.num1)} and {str(self.num2)} is {str(r)}"
    
    def mul(self):
        r = self.num1 * self.num2
        return f"the multipying of {str(self.num1)} and {str(self.num2)} is {str(r)}"
    
    def div(self):
        r = self.num1 / self.num2
        return f"the division of {str(self.num1)} and {str(self.num2)} is {str(r)}"     

if __name__ == "__main__":
    cal = calculator()
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())