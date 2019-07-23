points = 174  # use this as input for your submission

prize = "None"


# use the points value to assign prizes to the correct prize names

if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = "None"
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
    prize = "wafer-thin mint"
else:
    prize = "penguin"

if prize == "None":
    print("Oh dear, no prize this time.")
else:
    print("Congratulations! You won a {}!".format(prize))
