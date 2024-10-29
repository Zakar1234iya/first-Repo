from Animal import Animal
from Monkey import Monkey
from Lion import Lion
from Bear import Bear


class Zoo:
    def __init__(self, zoo_name):
        self.animal = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animal.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animal:
            animal.display_info()
            
            
            

            

# Create a zoo
Zak_zoo = Zoo("""
 ______     _      ______           
|___  /    | |    |___  /           
   / / __ _| | __    / / ___   ___  
  / / / _` | |/ /   / / / _ \ / _ \ 
 / /_| (_| |   <   / /_| (_) | (_) |
/_____\__,_|_|\_\ /_____\___/ \___/ 
              """)


# Add Animal to the zoo
Zak_zoo.add_animal(Lion("Nala", 9, 5))
Zak_zoo.add_animal(Lion("Simba", 9, 10))
Zak_zoo.add_animal(Monkey("Rafiki", 2, "Bananas"))
Zak_zoo.add_animal(Bear("Kenai", 7, "Brown"))

for animal in Zak_zoo.animal:
    if animal.name == "Simba":
        animal.feed()
           

# Display all animals' info
Zak_zoo.print_all_info()




