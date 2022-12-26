import pandas as pd

# Method 1

# will create a file names "filename.txt" in this current directory
with open(file="filename.txt", mode="w") as file:
    file.write("Subrata! successfully created this file.")

# Method 2

cities = ["Kolkata", "Vadodara", "Delhi", "Bangalore"]
population = [5467338, 6483429, 647928, 6478928]

data = {
    "CITY": cities,
    "POPULATION": population
}

df = pd.DataFrame(data)
print(df)

# export file named : "pd_file.csv"
df.to_csv("pd_file.csv", index=False)
print(pd.read_csv("pd_file.csv"))
