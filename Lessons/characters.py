def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1
        # if you took out index line, infinate loop of "B"
        # increasing index allows us to get to an exit point for while loop


characters(msg="Bedtime")
# if you want all lower case... print Bedtime.lower()
