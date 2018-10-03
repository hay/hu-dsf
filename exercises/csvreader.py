paintings = open("../examples/paintings.csv")

for painting in paintings:
    painting = painting.split(",")
    title = painting[0]
    painter = painting[1]
    price = painting[2]
    print(title + ", painted by " + painter + " sold for " + price)
    
paintings.close()