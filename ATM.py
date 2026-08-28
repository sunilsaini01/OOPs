class ATM():
    #Constructor
    def __init__(self):
        self.pin = ''
        self.Balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
        Hi How Can I Help You
        1. press 1 to create pin
        2. press 2 to change pin                  
        3. press 3 to check Balance
        4. press 4 to withdraw
        5. anything else to exit""")
        
        
        if user_input == '1':
            self.create_pin()
        elif user_input =='2':
            self.change_pin()
        elif user_input == '3':
            self.check_Balance()
        elif user_input == '4':
            self.withdraw()    
        else:
            exit()
            
    def create_pin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin
        
        user_Balance = int(input('Enter Balance'))
        self.Balance = user_Balance
        
        print('pin created successfully')
        self.menu()
        
        
    def change_pin(self):
        old_pin = input('Enter your Old Pin')
        
        if old_pin == self.pin:
            new_pin = input('Enter new pin')
            self.pin = new_pin
            print("pin created successfully")
            self.menu()
            
        else:
            print("Incorrect Pin")
            
            self.menu()
            
    def check_Balance(self):
        user_pin = input('Enter your Pin')
        if user_pin == self.pin:
            print('your Balance', self.Balance)
            self.menu()
            
        else:
            print('Incorrect pin')
            self.menu()
    
    def withdraw(self):
        user_pin = input('Enter your pin')
        if user_pin == self.pin:
            amount = int(input('enter amount'))
            if amount <= self.Balance:
                self.Balance = self.Balance - amount
                print('withdraw successful. Balance is', self.Balance)
                
            else:
                print('Sorry insufficient Balance')
        else:
            print('Incorrect pin')
        
        self.menu()   
    
# Object
a = ATM()