"""For Loops Practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're a good boy!
for elem in pets:
    print(f"Good boy, {elem}!")
# for loops are nice because you avoid infinite loops


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # print(str(idx) + ":" + names[idx])
    print(f"{idx} : {names[idx]}")

nums: list[int] = [1, 2, 3]
for x in nums:
    print(x)
