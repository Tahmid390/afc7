class Robot:
    def __init__(self):
        self.tech = "new"

    def intro(self):
        print("I am a robot")

ob = Robot()
print(ob.tech)  
ob.intro()       