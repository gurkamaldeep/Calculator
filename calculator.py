#This is a script for a calculator that takes two values and enable
#the user to perform four basic operations add, sub, div, mul

class Calc:
    def __init__(self,nmbr1,nmbr2):
        self.nmbr1 = nmbr1
        self.nmbr2 = nmbr2

    def add(self):
        return self.nmbr1 + self.nmbr2      #addition

    def sub(self):
        return self.nmbr1 - self.nmbr2      #subtraction

    def mul(self):
        return self.nmbr1 * self.nmbr2      #multiplication

    def div(self):
        return self.nmbr1 / self.nmbr2      #division

print 'Welcome to my Calculator\n','Enter 0 to close '

#this loop enables it to run again and check if input is zero, it exits
while True:
    frstnmbr = int(raw_input('Enter the first number: '))
    if frstnmbr == 0 :
        break
    scndnmbr = int(raw_input('Enter the Second number: '))
    cal1 = Calc(frstnmbr,scndnmbr)
    option = raw_input('Enter the option\n'
                   '1. Addition\n'
                   '2. Subtraction\n'
                   '3. Multiplication\n'
                   '4. Division\n')
    if option == '1':
        print cal1.add()
    elif option == '2':
        print cal1.sub()
    elif option == '3':
        print cal1.mul()
    elif option == '4':
        print cal1.div()
    else:
        print 'Enter from the above options'
        break
        
