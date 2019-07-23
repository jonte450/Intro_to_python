def create_cast_list(filename):
    cast_list = []
    with open(filename) as file:
        for name in file:
            first_name = name.split(",")[0]
            cast_list.append(first_name)
        
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
