class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        self.ingredients[ingredient] = quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
