import pandas as pd
import matplotlib.pyplot as plt

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

# Plotting the distribution of the 'race' column
plt.figure(figsize=(10, 5))
df['race'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Race')
plt.xlabel('Race')
plt.ylabel('Count')
plt.show()

# Plotting the distribution of the 'age_cat' column
plt.figure(figsize=(10, 5))
df['age_cat'].value_counts().plot(kind='bar', color='lightcoral')
plt.title('Distribution of Age Categories')
plt.xlabel('Age Category')
plt.ylabel('Count')
plt.show()

# Plotting the distribution of the 'sex' column
plt.figure(figsize=(8, 5))
df['sex'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Distribution of Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
