import extraction
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'workout_data.csv' with the path to your exported workout data
df = pd.read_csv('workout_data.csv', parse_dates=['start_date', 'end_date'])


#PSA: Can inoly run one example at a time

# Example 1. Plot workouts per day based on start_date
daily_workouts = df.groupby(df['start_date'].dt.date).size()
plt.figure(figsize=(10, 5))
daily_workouts.plot(kind='line')
plt.title('Daily Workouts Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Workouts')
plt.show()


# Example 2. Plot most used units 
unit_counts = df['unit'].value_counts()
plt.figure(figsize=(8, 8))
unit_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Units in Workout Data')
plt.ylabel('')
plt.show()
