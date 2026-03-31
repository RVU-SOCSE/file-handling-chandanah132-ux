import pandas as pd

# Step 1: Read the CSV file
# Replace 'data.csv' with your actual file name
df = pd.read_csv('C:/Users/RVUW278/Downloads/5prog_1experience.csv')

# 1. Display the content of the file
print("Full DataFrame:\n")
print(df)

# 2. Find total number of rows and columns
rows, cols = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", cols)

# 3. Calculate the length of the dataframe
print("\nLength of DataFrame:", len(df))

# 4. Display first 2 rows only
print("\nFirst 2 rows:\n")
print(df.head(2))
