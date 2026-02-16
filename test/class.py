class Phone:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
    def charge(self):
        print(f"Your {self.model} is charging")
    def wake_up(self):
        print(f"Your {self.model} woked up")
    def describe(self):
        print(f"Your phone model is {self.model}, color: {self.color}, and cost ${self.price}")

phone = Phone("Xiaomi 15", 599.99, "Red")
phone1 = Phone("Xiaomi 14", 699.99, "Red")
phone2 = Phone("Xiaomi 16", 799.99, "Red")

phone2.describe()
