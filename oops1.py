# initiate a class 
class employee:
    #special method/magic method/ dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary =50000
        self.designation = "AI Engineer"
        
        
    #method  
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")
        
        
# creating an object/ instance of the class
sam = employee()

# printing the attributes
# print(sam.id)
# print(sam.salary)

sam.travel("Kerala")