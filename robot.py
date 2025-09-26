class Robot:
   
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)
    def walk(self, x):
        self.position[0] = self.position[0] + x
        

    def eat(self):
        print("I'm hungry!")

class Robot_Dog(Robot):
    
     

    def eat(self):
        super().eat()
        print('I like bacon!')

# Main program
my_robot_dog = Robot_Dog('Bud') 
my_robot_dog.eat()
