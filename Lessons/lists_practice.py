"""List Practice"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# add an item to the list
my_numbers.append(1.5)  # adding 1.5 to list of my_numbers
my_numbers.append(1.4)

# create an already populated list
game_points: list[int] = [102, 86, 94]
# print(game_points)

# subscription notation/indexing
# print(game_points[2])  # indexing and printing out just number 94, index 2

# modifying by index - changing 86 to 72
game_points[1] = 72
# print(game_points)

# getting the length
print(len(game_points))
y: int = len(game_points)  # can also assign length as a variable
# print(y)

# remove an item from a list
game_points.pop(1)
# print(game_points)

# write a function called display
# input: list[int]
# return: None
# Loop over input and print every value
# Try calling it on game_points


def display(Input: list[int]) -> None:
    index: int = 0
    while index < len(Input):
        print(Input[index])
        index += 1


display(Input=game_points)
