# Question - Classifying Age 
class Person:
    def __init__(self,initialAge):        
        if initialAge<=0:
            print("Age is not valid, setting age to 0.")
            age=initialAge
        
    def amIOld(self):
        if age<13:
            print("You are young.")
        elif age>=13 and age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
                    
    def yearPasses(self):
        global age 
        age+=1
