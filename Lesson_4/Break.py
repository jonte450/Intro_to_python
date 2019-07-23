# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
iteration = 0

while iteration < len(headlines):
    news_ticker += headlines[iteration] + " "
    if len(news_ticker)>=140:
        news_ticker = news_ticker[:140]
        break
    iteration += 1

        
print(len(news_ticker))
print(news_ticker)
