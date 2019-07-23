points = 174  # use this input to make your submission

result = "" 

if points>=1 and 51 > points:
    result = "Congratulations! You won a wooden rabbit!"

elif points>=51 and points < 151:  
    result = "Oh dear, no prize this time."
    
elif points>=151 and points < 181:  
    result = "Congratulations! You won a wafer-thin mint!"

elif points>=181 and points <= 200:   
    result = "Congratulations! You won a penguin!"

print(result)



