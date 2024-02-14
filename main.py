# ################################################################################
#
# ███████  ██████ ███████     ██████  ███████  ██  ██████  
# ██      ██      ██               ██      ██ ███ ██  ████ 
# █████   ██      █████        █████      ██   ██ ██ ██ ██ 
# ██      ██      ██               ██    ██    ██ ████  ██ 
# ███████  ██████ ███████     ██████     ██    ██  ██████  
# 
# Project Created by: Morgan Molyneaux, Kamilla Turapova, Sioelli Olive
# 
# Purpose:
# This program analyzes a CDC dataset, detailing health and habits of individuals, ect...
# It calculates the IQR for height and age, and evaluates relative frequencies.
#
# Features:
# - Compute Interquartile Range (IQR) for height and age
# - Determine relative frequency distributions for 'gender' and 'exerany'
# - Visualize data insights through plots and statistics
#
################################################################################
import pandas as pd 
import matplotlib.pyplot as plt

def BarPlot():
    ''' This function will create a barplot of relative frequency for gender and exercise.
    Then computes the proportion for gender and exercise, and prints results to the console.'''
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
    
    # Gets frequency of proportion of sample that is female (noted at 'f' in the csv file)
    prop_female = gender_freq.get('f', 0)  
    print("                       Question 1.B")
    print("---------------------------------------------------------------")
    print(f"ii. What proportion of the sample is female: {prop_female:.2f}")
    # Proportion that has exercised in the past month (noted at '1' in the csv file for yes, and '0' for no)
    prop_exercised = exerany_freq.get(1, 0)  
    print(f"iii. What proportion has exercised in the past month: {prop_exercised:.2f}")
    print("--------------------------------------------------------------- \n")

def BoxPlot():
    ''' This function will create a boxplot for height and age.  Then computes the IQR 
    for each, and prints results to the console'''
    plt.boxplot([csv_data["height"], csv_data["age"]], labels=["Height", "Age"])
    plt.show()
    
    # Caclulate the IQR for height 
    q1_height = csv_data['height'].quantile(0.25)
    q3_height = csv_data['height'].quantile(0.75)
    iqr_height = q3_height - q1_height
    print("          Question 1.A")
    print("|-----------------------------|")
    print(f"     IQR for Height: {iqr_height}")

    # Caclulate the IQR for age
    q1_age = csv_data['age'].quantile(0.25)
    q3_age = csv_data['age'].quantile(0.75)
    iqr_age = q3_age - q1_age
    print(f"     IQR for Age: {iqr_age}")
    print("|-----------------------------| \n")
    
# Load the data from CSV file into temp variable
csv_data = pd.read_csv('cdc.csv')

# Barplot deployed to visualize the relative frequency & boxplot for height and age.
BoxPlot()
BarPlot()


# Shows the crosstab between smoking habits and gender. 
crosstab = pd.crosstab(csv_data['gender'], csv_data['smoke100'])
print("                 Question 2")
print("------------------------------------------ ")
print(crosstab, "\n")


# Find the mean and standard deviation of weight:
weight_mean = csv_data["weight"].mean()
weight_std = csv_data["weight"].std()

print("               Question 3.A")
print("|------------------------------------------|")
print("            Mean Weight:", weight_mean)
print(f"   Standard Deviation of Weight: {weight_std:.5f}")
print("|------------------------------------------| \n")

# Calculate the bounds for one standard deviation
lower_bound = weight_mean - weight_std
upper_bound = weight_mean + weight_std

# Count the number of weights within one standard deviation
weights_within_one_std = csv_data[(csv_data["weight"] >= lower_bound) & (csv_data["weight"] <= upper_bound)].shape[0]
total_weights = csv_data.shape[0]

# Calculate the proportion of weights within one standard deviation
proportion_within_one_std = weights_within_one_std / total_weights
print("               Question 3.B")
print("|------------------------------------------|")
print("Proportion of weights within one standard deviation:", proportion_within_one_std)
print("|------------------------------------------|")
