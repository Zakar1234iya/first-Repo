class Animal:
    def __init__(self , name ,age , health=0 , happiness_level=0 ) :
        self.name = name 
        self.age = age 
        self.health = health
        self.happiness = happiness_level

    def display_info(self):
        print(f"name is {self.name} , Health = {self.health} , happiness = {self.happiness}")

    def feed(self):
        self.happiness += 10
        self.health += 10


  



       

    





 