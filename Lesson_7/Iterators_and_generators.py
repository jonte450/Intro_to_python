lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    counter = start
    for elem in iterable:
        yield counter,elem
        counter = counter + 1
        
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i,lesson))

def chunker(iterable, size):
    for i in range(0, len(iterable),size):
        yield iterable[i:(i+size)]


for chunk in chunker(range(25), 4):
    print(list(chunk))
