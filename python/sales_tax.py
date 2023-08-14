# practice creating a class with attributes and a method


class PurchasedGood:
    def __init__(self, price, category="General", tax=0.07) -> None:
        self.price = price
        self.category = category
        self.tax = tax

    def calculate_total(self):
        return round(self.price * (1 + self.tax), 2)
