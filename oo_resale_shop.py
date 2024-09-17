# Rachel Michaud - I did not collaborate with anyone on this assignment
# I did not utilize any outside sources 
from computer import *
class ResaleShop:

    
    # What attributes will it need?
    #inventory: list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        # Inventory is defined 
        self.inventory = []
    
    # What methods will you need?
    # Prints out each item in the inventory by calling method from computer.py
    def printOut(self):
        if len(self.inventory):
            print("Inventory: ")
            for computer in self.inventory:
                computer.printdetails()
    
    # Updates the price of the computer depending on the year
    # Updates the OS if necessary
    def refurbish_inv(self, computer, new_os):
        if computer in self.inventory:
            if computer.year_made < 2000: 
                computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
            else:
                computer.price = 1000

            if new_os is not None:
                computer.operating_system = new_os
        else:
            print(computer, "not found. Please select another item to refurbush.")
    
    # Removes the computer if it is in the inventory and sold 
    def sell_computer(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Sorry, this computer is not in stock.")

    # Adds a new computer to the inventory 
    def buy_computer(self, computer: Computer):
        self.inventory.append(computer)

def main():
    # Creates two new computers 
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    computer2 = Computer(
    "COMP2Mac  Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 82,
    "macOS Big Sur", 2022, 1500
    )

    # Testing the methods 
    shop = ResaleShop()
    shop.buy_computer(computer)
    shop.buy_computer(computer2)
    shop.printOut()
    shop.refurbish_inv(computer2, "new OS")
    shop.sell_computer(computer)
    shop.sell_computer(computer)
    shop.printOut()

if __name__ == "__main__":
    main()


