class Burger:
    number = 0
    total_price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Burger.number += 1
        Burger.total_price += price

 #INSTANCE METHOD
    def get_info(self):
        return f"{self.number}. {self.name}: ${self.price}"
 #CLASS METHOD
    @classmethod
    def get_nmb(cls):
        return f"Total # of burgers: {cls.number}"
    @classmethod
    def get_total(cls):
        return f"Total $ of burgers: ${cls.total_price}"
    @classmethod
    def get_avg(cls):
        if cls.number == 0:
            return 0
        else:
            return f"Average $ of burgers: ${cls.total_price / cls.number}"

burger = Burger("Cheeseburger", 2.99)
burger1 = Burger("Hamburger", 3.99)
burger2 = Burger("Chickenburger", 4.99)
burger3 = Burger("Burger", 1.99)
print(Burger.get_total())
