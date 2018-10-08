movie = {
    "title" : "Blade Runner",
    "year" : 1982,
    "duration" : 117,
    "director" : "Ridley Scott"
}

movie["actors"] = ["Harrison Ford", "Rutger Hauer", "Sean Young"]

for key in movie:
    value = movie[key]

    if key == "duration":
        value = f"{value} minutes"

    if key == "actors":
        value = ", ".join(value)

    print(f"{key}: {value}")