# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:\\Users\\aaris\\OneDrive\\Documents\\data\\delhiaqi.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Data Overview:")
print(df.head())

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extracting month for seasonal analysis
df['month'] = df['date'].dt.month

# Descriptive statistics for key pollutants
pollutants = ['co', 'no', 'no2', 'so2', 'pm2_5', 'pm10', 'nh3']
print("\nDescriptive Statistics for Key Pollutants:")
print(df[pollutants].describe())

# Analyzing seasonal variations
monthly_avg = df.groupby('month')[pollutants].mean()
print("\nMonthly Average Pollutants:")
print(monthly_avg)

# Plotting monthly average levels of pollutants
plt.figure(figsize=(12, 8))
for pollutant in pollutants:
    plt.plot(monthly_avg.index, monthly_avg[pollutant], marker='o', label=pollutant)
plt.title('Monthly Average Levels of Pollutants in Delhi')
plt.xlabel('Month')
plt.ylabel('Average Concentration')
plt.xticks(monthly_avg.index)
plt.legend()
plt.grid()
plt.show()

# Correlation analysis between pollutants
plt.figure(figsize=(10, 8))
corr = df[pollutants].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Pollutants')
plt.show()

# Identifying peak pollution months
peak_months = monthly_avg.idxmax()
print("\nMonths with Peak Pollution Levels:")
print(peak_months)

# Creating a box plot to visualize the distribution of PM2.5 levels
plt.figure(figsize=(10, 6))
sns.boxplot(x='month', y='pm2_5', data=df)
plt.title('PM2.5 Levels Distribution by Month')
plt.xlabel('Month')
plt.ylabel('PM2.5 Concentration')
plt.grid()
plt.show()

# Public Health Implications
print("\nPublic Health Insights:")
print("High levels of PM2.5 during winter months may lead to respiratory problems.")
print("NO2 levels also spike in winter, linked to increased vehicular emissions.")
print("Recommendations: Implement stricter vehicular emissions standards and promote public transport.")

# Saving the cleaned data to a new CSV for future reference
output_file_path = "C:\\Users\\aaris\\OneDrive\\Documents\\data\\cleaned_delhiaqi.csv"
df.to_csv(output_file_path, index=False)
print(f"\nCleaned data saved to: {output_file_path}")
