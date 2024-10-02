"""Tea Party Planner!"""

__author__: str = "730684336"


def main_planner(guests: int) -> None:
    """Printing all the functions that are defined below from guests parameter."""
    # Need to make sure everything is a str to concatenate!!
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Need to make sure its str(guests) not str(int) because guests is the parameter
    print("Tea Bags" + ": " + str((tea_bags(people=guests))))
    print("Treats" + ": " + str((treats(people=guests))))
    print(
        "Cost"
        + ": "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


# Define main_planner before the rest of the functions, easier to read

# To get spaces between : and number in trailhead, add a space before the end quote
# Why is it seperating line 12 like that?
# Office Hours- TA said the line seperation is okay


def tea_bags(people: int) -> int:
    """Finding the number of tea bags that are needed based on the number of people."""
    return int(people * 2)


def treats(people: int) -> int:
    """Finding the number of treats needed for the tea party."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Sum of tea and treats to get total cost of tea party."""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
