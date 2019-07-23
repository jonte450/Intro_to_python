names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [first_name.split()[0].lower() for first_name in names]
print(first_names)

multiples_3 = [multi_3*3 for multi_3 in range(1,21,1)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [key for key,value in scores.items() if scores[key]>65]
print(passed)
