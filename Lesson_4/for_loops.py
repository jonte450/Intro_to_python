sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for sen in sentence:
    print(sen)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for five in range(5,31,5):
    print(five)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for user in names:
    user_name = user.replace(' ','_')
    usernames.append(user_name.lower())


print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for user in range(len(usernames)):
    user_name = usernames[user].replace(' ','_')
    usernames[user] = user_name.lower()
   
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for check in tokens:
    first = check[0]
    last = check[len(check)-1]
    if first == '<' and last == '>':
        count += 1

print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

for html in items:
    new_html = "<li>"+html+"</li>"+"\n"
    html_str += new_html

html_str += "</ul>"
print(html_str)
