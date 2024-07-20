import pandas as pd
import matplotlib.pyplot as plt
import glob
from app.config.configuration import Config
import os

def plot(config: Config):
    # Path pattern for the weekly report CSV files
    file_pattern = os.path.join(config.resource_dir, 'weekly', "report_week_*.csv")

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
    weekly_wasted_time = combined_data.groupby('week')['Duration'].sum().reset_index()

    # Convert the summed durations to total hours for easier plotting
    weekly_wasted_time['Duration'] = weekly_wasted_time['Duration'].dt.total_seconds() / 3600

    # Ensure all weeks from 1 to 29 are included, with 0 hours for missing weeks
    all_weeks = pd.DataFrame({'week': range(1, 30)})
    # delete the below 2 lines. TODO
    all_weeks.to_csv('all_weeks.csv', index=False)
    weekly_wasted_time.to_csv('weekly_wasted_time.csv', index=False)
    weekly_wasted_time = pd.merge(all_weeks, weekly_wasted_time, on='week', how='left').fillna(0)

    # Plot the dependency of wasted time over weeks
    plt.figure(figsize=(10, 6))
    plt.plot(weekly_wasted_time['week'], weekly_wasted_time['Duration'], marker='o')
    plt.title('Wasted Time Over Weeks')
    plt.xlabel('Week')
    plt.ylabel('Wasted Time (Hours)')
    plt.grid(True)
    plt.xticks(weekly_wasted_time['week'])
    plt.tight_layout()

    plt.savefig("wasted_time_over_weeks.png")
    plt.show()

if __name__ == '__main__':
    config = Config()
    plot(config)
