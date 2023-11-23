import pandas as pd

# Load data from CSV file
file_path = "cox-violent-parsed_filt_usable.csv"
df = pd.read_csv(file_path)

# Display basic information about the data
print(df.info())

# Display descriptive statistics
print(df.describe())

# Display the distribution of the 'race' column
print(df['race'].value_counts())

# Display the distribution of the 'age_cat' column
print(df['age_cat'].value_counts())

# Display the distribution of the 'sex' column
print(df['sex'].value_counts())
