# Import the library
import pandas as pd

# Read the JSON file to a Dataframe
df = pd.read_json("movies.json")

# Select only movies that were made in 1983
df_1983 = df[df["year"] == 1983]

# Drop the 'actors' and 'genres' columns
del df_1983["actors"]
del df_1983["genres"]

# Save to a new CSV file
df_1983.to_csv("movies_1983.csv")