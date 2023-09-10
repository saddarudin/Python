class Computer:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"The name of the brand is {self.brand}, model is {self.model} and price is {self.price}")


my_computer = Computer("HP", 2019, 80)
my_computer.show_details()
