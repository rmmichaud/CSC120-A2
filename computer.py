# Rachel Michaud - I did not collaborate with anyone on this assignment
# I did not utilize any outside sources 
class Computer:

    # What attributes will it need?
    # Attributes are defined below
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        # Defines the attributes 
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def printdetails(self):
        # Print out computer details
        print(self.description , ",", self.processor_type, ",", self.hard_drive_capacity
            , "," , self.memory , "," , self.operating_system , "," 
            , self.year_made , "," , self.price)
    
def main():
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    # Computer is printed 
    computer.printdetails()

#only call main() if I am running this program directly 
if __name__ == "__main__":
    main()