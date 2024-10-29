from Animal import Animal

class Monkey(Animal):
    def __init__(self, name, age, favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def display_info(self):
        super().display_info()
        print(f"Favorite Food: {self.favorite_food}")