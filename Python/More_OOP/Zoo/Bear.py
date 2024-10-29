from Animal import Animal

class Bear(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")
