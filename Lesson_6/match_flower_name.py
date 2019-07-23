def create_flower_dict():
    flowers_dict = {}
    with open("flowers.txt") as file:
        all_flowers = file.readlines()

        for flower in all_flowers:
            flower = flower.split(":")
            name = flower[1].rstrip("\n ")
            flower[1] = name.lstrip()
            flowers_dict[flower[0]] = flower[1]
    return flowers_dict

def user_input(dict):
    while True:
        name = input("Enter your First [space] Last name only:").title().split(" ")
        first_name = name[0]
        letters = first_name[0]
        flower_char = letters[0]
        flower = dict[flower_char]
        if flower_char not in dict:
            print("Sorry try to write in your full name with the first letter with an capital_letter!")
        else:
            print("Unique flower name with the first letter: {}".format(flower))

#create a function to ask for user's first and last name
dict = create_flower_dict()
user_input(dict)

