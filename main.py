import pandas as pd 
import matplotlib.pyplot as plt


# Load the data from CSV file into temp variable
csv_data = pd.read_csv('cdc.csv')

# Print the data
plt.boxplot([csv_data["height"], csv_data["age"]], labels=["Height", "Age"])
plt.show()

