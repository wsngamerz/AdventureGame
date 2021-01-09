class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super().__init__(name, description, value)
        self.damage = damage


class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", "A Small, Lightweight Dagger", 10, 2)


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", "A Sword with a string steel blade", 75, 10)

class Coin(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__("Gold Coins", f"A pouch filled with { self.amount } gold coins", self.amount)
