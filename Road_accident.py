import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("road_accident_data.csv")

# Display Dataset
print(data.head())

# Total Accidents
total_accidents = len(data)

print("Total Accidents:", total_accidents)

# Accident Severity Count
severity_count =
    data['Accident_Severity'].value_counts()

print(severity_count)

# Plot Severity Chart
severity_count.plot(kind='bar')

plt.title("Accident Severity Analysis")

plt.xlabel("Severity")

plt.ylabel("Number of Accidents")

plt.show()

# Vehicle Type Analysis
vehicle_count =
    data['Vehicle_Type'].value_counts()

vehicle_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Vehicle Type Distribution")

plt.show()
