import pandas as pd
import csv

# Read the data from your file
with open('scopus_publications.csv', 'r', encoding='latin1') as file:
    data = file.read()


# Split the data into rows based on semicolons
rows = [row.strip() for row in data.split('\n')]

# Identify column names from the first row
column_names = rows[0].split('\t')

# Create a DataFrame
data_values = [row.split('\t') for row in rows[1:]]
df = pd.DataFrame(data_values, columns=column_names)

# Display the DataFrame
print(df)

# Save the DataFrame to a new CSV file
df.to_csv('organized_scopus_publications.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
