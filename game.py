class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.inventory = []

    def __repr__(self):
        for item in self.inventory:
            print(item)

    def add_item(self, item):
        self.inventory.append(item)


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display_item_stats(self):
        print(f"Name: {self.name}, Value: {self.value}")


sword = Item("sword", 200)
axe = Item("axe", 220)
hammer = Item("hammer", 190)
items = [sword, axe, hammer]

# for item in items:
#     print(item.display_item_stats())

class ItemView:
    def __init__(self)
    
player = Player("jadon")
player.add_item(sword)
player.__repr__()


class ShopKeeper:
    def __init__(self):
        self.store_items = items

    def display_inv(self):
        for item in self.store_items:
            print(item)

    def remove_item(self, item):
        self.store_items.pop(item)
        return self.store_items


# shop_inv = ShopKeeper.display_inv()
# print(shop_inv)


def landing_screen():
    print("Welcome to Namatashi no sekai")


# items = {"Katana": 275, "Short Sword": 180, "Legendary Dagger": 480}

# for item in items:
#     key = items[item]
#     print(key)
#     print(item)
