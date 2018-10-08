import json

with open("movies.json") as f:
    movies = json.load(f)

print("Choose an option to list all movies...:")
print("1: from a given year")
print("2: longer than a certain duration")
print("3: where the director is also an actor in the movie")
choice = input("What's your choice? ")

if choice not in ["1", "2", "3"]:
    print("Invalid choice!")
    exit()

if choice == "1":
    user_year = int(input("Give a year: "))
    
if choice == "2":
    user_duration = int(input("Give a duration: "))
        
for movie in movies:
    year = movie["year"]
    title = movie["title"]
    duration = movie["duration"]
    director = movie["director"]
    
    if choice == "1" and movie["year"] == user_year:
        print(f"'{title}' is from {year}")
    
    if choice == "2" and movie["duration"] > user_duration:
        print(f"'{title}' is {duration} minutes long")
        
    if choice == "3" and movie["director"] in movie["actors"]:
        print(f"'{title}' has {director} as an actor as well")