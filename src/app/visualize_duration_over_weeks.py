import pandas as pd
import matplotlib.pyplot as plt
import glob
from app.config.configuration import Config
import os

def plot(config: Config):
    # Path pattern for the weekly report CSV files
    file_pattern = os.path.join(config.resource_dir, 'weekly_entries', "week_duration_*.csv")

    # Read all CSV files matching the pattern
    all_files = glob.glob(file_pattern)
    if not all_files:
        print('No weekly report files found. Please run the data fetching script first. Script: get_online_csv_report_over_weeks.py')
        return
    # Initialize an empty DataFrame to hold the combined data
    combined_data = pd.DataFrame()

    # Iterate over each file and append its data to the combined DataFrame
    for file in all_files:
        df = pd.read_csv(file)
        # Extract week number from the file name and add it as a new column
        week_number = int(file.split('_')[-1].split('.')[0])
        df['week'] = week_number
        combined_data = pd.concat([combined_data, df], ignore_index=True)

    # Save the combined data to a CSV file
    combined_data.to_csv('combined_data.csv', index=False)

    # Convert the 'Duration' column to timedelta
    combined_data['Duration'] = pd.to_timedelta(combined_data['Duration'])

    # Group by 'week' and sum the 'Duration'
    weekly_hours = combined_data.groupby('week')['Duration'].sum().reset_index()

    # Convert the summed durations to total hours for easier plotting
    weekly_hours['Duration'] = weekly_hours['Duration'].dt.total_seconds() / 3600

    # Ensure all weeks from 1 to 29 are included, with 0 hours for missing weeks
    all_weeks = pd.DataFrame({'week': range(1, 30)})
    weekly_hours = pd.merge(all_weeks, weekly_hours, on='week', how='left').fillna(0)

    # Plot the dependency of wasted time over weeks
    plt.figure(figsize=(10, 6))
    plt.plot(weekly_hours['week'], weekly_hours['Duration'], marker='o')
    plt.title('Duration Over Weeks')
    plt.xlabel('Week')
    plt.ylabel('Duratoin (Hours)')
    plt.grid(True)
    plt.xticks(weekly_hours['week'])
    plt.tight_layout()

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.join(config.resource_dir, 'output'), exist_ok=True)

    # Save the plot as an image file
    plt.savefig(os.path.join(config.resource_dir, 'output', 'duration_over_weeks.png'))
    plt.show()

if __name__ == '__main__':
    config = Config()
    plot(config)
