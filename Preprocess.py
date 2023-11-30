import pandas as pd

# Read the data
df = pd.read_csv('organized_scopus_publications.csv', encoding='latin1')
df.to_csv('D:\Superior\Smester 7\Data Science\Assignment4\preprocessed_scopus_publications.csv', index=False, encoding='utf-8')

# Data Cleaning and Preprocessing for Text Columns
text_columns = ['Author full names', 'Title', 'Link', 'Affiliations', 'Authors with affiliations']

# Fill missing values in text columns with empty strings
df[text_columns] = df[text_columns].fillna('')

# Text cleaning and processing for specific columns
df['Title'] = df['Title'].str.replace('[^\w\s]', '').str.lower()

# Handling categorical data (example: 'Affiliations')
df['Affiliations'] = df['Affiliations'].astype('category')

# Save the preprocessed data to a new CSV file
df.to_csv('preprocessed_scopus_publications.csv', index=False, encoding='utf-8')

print("Preprocessing completed. Preprocessed data saved to 'preprocessed_scopus_publications.csv'.")
