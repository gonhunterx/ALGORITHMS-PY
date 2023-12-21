# Classes
class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.inventory = {}

    def display_stats(self):
        print(self.name)
        for item in self.inventory:
            print(f"- {item.value()}")
        print(self.gold)


def main():
    print("Welcome to Nematashi Yameru")
