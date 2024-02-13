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

# I think this is how we are able to find mean using the matplotlib libary. 
test = csv_data["height"].mean()
print(test)



plt.show()

