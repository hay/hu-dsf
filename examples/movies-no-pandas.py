# Import json and csv libraries
import json
import csv

# Open movies.json and convert to a list of dicts
with open("movies.json") as f:
    movies = json.load(f)

# Also create a new list to hold the filtered movies
new_movies = []

# Loop over movies
for movie in movies:
    # Delete the 'actors' and 'genres' keys
    del movie["actors"]
    del movie["genres"]

    # Check if year is 1983
    if movie["year"] == 1983:
        # Add to the new list
        new_movies.append(movie)

# Open the 'movies_1983.csv' file for writing
with open("movies_1983.csv", "w") as f:
    # Get the fieldnames, this is required when also writing a header
    # We get them from the first item in new_movies
    fieldnames = new_movies[0].keys()

    # Create a new CSV 'dictionary writer'
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    # Loop over the movies in the new_movies list
    for row in new_movies:
        # And write them to the CSV file
        writer.writerow(row)