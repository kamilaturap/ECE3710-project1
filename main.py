import pandas as pd 
import matplotlib.pyplot as plt


# Load the data from CSV file into temp variable
csv_data = pd.read_csv('cdc.csv')

# Print the data
plt.boxplot([csv_data["height"], csv_data["age"]], labels=["Height", "Age"])

q1_height = csv_data['height'].quantile(0.25)
q3_height = csv_data['height'].quantile(0.75)
iqr_height = q3_height - q1_height
print(f"IQR for Height: {iqr_height}")

q1_age = csv_data['age'].quantile(0.25)
q3_age = csv_data['age'].quantile(0.75)
iqr_age = q3_age - q1_age
print(f"IQR for Age: {iqr_age}")

plt.show()

