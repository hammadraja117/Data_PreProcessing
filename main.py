import pandas as pd
import csv

# Read the preprocessed data
df = pd.read_csv('preprocessed_scopus_publications.csv', encoding='utf-8')

# Filter publications affiliated with Superior University and the specified departments
superior_publications = df[df['Affiliations'].str.contains("superior university", case=False) &
                           (df['Affiliations'].str.contains(r'\bcomputer science\b', case=False) |
                            df['Affiliations'].str.contains(r'\binformation technology\b', case=False) |
                            df['Affiliations'].str.contains(r'\bsoftware engineering\b', case=False))]

# Write the filtered data to a new CSV file
superior_publications.to_csv('filtered_superior_publications.csv', index=False, encoding='utf-8')

print("Filtered publications from Superior University with specified departments have been saved to 'filtered_superior_publications.csv'.")
