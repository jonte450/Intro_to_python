x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
cord = ""
# write your for loop here
iterate = 0
for x,y,z in zip(x_coord,y_coord,z_coord):
        cord = labels[iterate]+": "+str(x)+", "+str(y)+", "+str(z)
        points.append(cord)
        iterate += 1

for point in points:
    print(point)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = {}

for actor,height in zip(cast_names,cast_heights):
    cast[actor] = height
print(cast)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = []
heights = []


names, heights = zip(*cast)

print(names)
print(heights)


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = []

data_transpose = tuple(zip(*data))
print(data_transpose)


cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]



for h,actor in enumerate(cast):
    cast[h] = actor + " " + str(heights[h])

print(cast)
