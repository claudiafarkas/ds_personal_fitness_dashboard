import xml.etree.ElementTree as ET
import pandas as pd


# Load and parse the XML file
tree = ET.parse('/Users/Claudia/Library/CloudStorage/OneDrive-Personal/personal_fitness_dashboard/apple_health_export/export.xml')
root = tree.getroot() 

# Dict to store the workout types that interest me
workout_types = {
    'HKWorkoutTypeIdentifier', # This is the general workout identifier
    'HKQuantityTypeIdentifierDistanceWalkingRunning',
    'HKQuantityTypeIdentifierBasalEnergyBurned',
    'HKQuantityTypeIdentifierActiveEnergyBurned',
    'HKQuantityTypeIdentifierDistanceCycling',
    'HKQuantityTypeIdentifierFlightsClimbed',
    'HKQuantityTypeIdentifierAppleExerciseTime',
    'HKQuantityTypeIdentifierAppleStandTime',
    'HKQuantityTypeIdentifierWalkingSpeed',
    'HKCategoryTypeIdentifierAppleStandHour',
    'HKQuantityTypeIdentifierHeartRate',
}

# Define a list to contain the workout data
workout_data = []

# Iterate over the records and filter for workouts
for record in root.findall('.//Record'):
    # print("\nHere are the records found: ", record in root.findall('.//Record'))
    record_type = record.get('type')
    # print("\nHere are the record types found:", record_type)
    if record_type in workout_types:
        # Extract the attributes of interest related to the workout types
        workout_data.append({
            'type': record_type,
            'source_name': record.get('sourceName'),
            'device': record.get('device'),
            'unit': record.get('unit'),
            'creation_date': record.get('creationDate'),
            'start_date': record.get('startDate'),
            'end_date': record.get('endDate'),
            'value': record.get('value'),
            'total_distance': record.get('totalDistance'),
            'total_distance_unit': record.get('totalDistanceUnit'),
            'workout_activity_type': record.get('workoutActivityType'),
            'duration':record.get("duration"),
            'duration_unit': record.get("durationUnit"),
            'avg': record.get('average'),
        })

# Convert the list to a DataFrame
df = pd.DataFrame(workout_data)

# Convert date strings to datetime objects
df['creation_date'] = pd.to_datetime(df['creation_date'])
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# Now `df` contains only workout data and is ready for to be saved to CSV
print(df.head(20))
df.to_csv('workout_data.csv', index=False)
print("Updated CSV file!")
