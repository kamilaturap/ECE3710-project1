import pandas as pd 
import matplotlib.pyplot as plt


# Load the data from CSV file into temp variable
csv_data = pd.read_csv('cdc.csv')

# Print the data
plt.boxplot([csv_data["height"], csv_data["age"]], labels=["Height", "Age"])

# Caclulate the IQR for height 
q1_height = csv_data['height'].quantile(0.25)
q3_height = csv_data['height'].quantile(0.75)
iqr_height = q3_height - q1_height
print(f"IQR for Height: {iqr_height}")

# Caclulate the IQR for age
q1_age = csv_data['age'].quantile(0.25)
q3_age = csv_data['age'].quantile(0.75)
iqr_age = q3_age - q1_age
print(f"IQR for Age: {iqr_age}")

# Used to count occurences of each value in the column (for Gender and Exerany)
gender_freq = csv_data['gender'].value_counts(normalize=True)
exerany_freq = csv_data['exerany'].value_counts(normalize=True)

# Subplot for gender size 
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
gender_freq.plot(kind='bar', color=['blue', 'pink'])
plt.title('Relative Frequency Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Relative Frequency')

# Subplot for exerany data
plt.subplot(1, 2, 2) # This must be 1, 2, 2 because we have 1 row and 2 columns, anything less will not show graph on layout. 
exerany_freq.plot(kind='bar', color=['green', 'red'])
plt.title('Relative Frequency Distribution for Exercise')
plt.xlabel('Exercised in the Past Month')
plt.ylabel('Relative Frequency')
plt.xticks(ticks=[0, 1], labels=['Yes', 'No'], rotation=0) 

plt.tight_layout()
plt.show()

# Shows the crosstab between smoking habits and gender. 
crosstab = pd.crosstab(csv_data['gender'], csv_data['smoke100'])
print(crosstab)
