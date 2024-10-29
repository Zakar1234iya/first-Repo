from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age, dangerous_level):
        super().__init__(name, age)
        self.dangerous = dangerous_level
        
    def display_info(self):
        super().display_info()
        print(f"dangerous: {self.dangerous}")