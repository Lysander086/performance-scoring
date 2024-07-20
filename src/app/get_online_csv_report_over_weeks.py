import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
# Define cookies and headers
import json
from app.config.configuration import Config
# Load environment variables from .env file
load_dotenv()
cookies = json.loads(os.getenv('TOGGL_COOKIE'))

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# Function to get report data for a given week


def get_report_data(start_date, end_date):
    json_data = {
        'collapse': True,
        'grouping': 'projects',
        'sub_grouping': 'time_entries',
        'end_date': end_date.strftime('%Y-%m-%d'),
        'start_date': start_date.strftime('%Y-%m-%d'),
        'audit': {
            'show_empty_groups': False,
            'show_tracked_groups': True,
            'group_filter': {},
        },
        'date_format': 'MM/DD/YYYY',
        'duration_format': 'classic',
        'hide_amounts': True,
        'hide_rates': True,
        'order_by': 'title',
        'order_dir': 'asc',
    }

    response = requests.post(
        'https://track.toggl.com/reports/api/v3/workspace/3661757/summary/time_entries.csv',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response

# Main function to iterate through weeks 1 to 29


def fetch_reports_for_weeks(config: Config):
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
    one_week = timedelta(weeks=1)

    for week in range(29):
        end_date = start_date + one_week - timedelta(days=1)
        print(
            f'Fetching data from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}')
        response = get_report_data(start_date, end_date)
        # Here, you can handle the response as needed, e.g., save to file or process further

        # Create directory if it doesn't exist
        os.makedirs(os.path.join(config.resource_dir, 'weekly_entries'), exist_ok=True)
        
        # Save response content to file
        with open(os.path.join(config.resource_dir, 'weekly_entries', f'report_week_{week+1}.csv'), 'wb') as f:
            f.write(response.content)
        start_date += one_week


# Call the function to fetch data
if __name__ == '__main__':
    fetch_reports_for_weeks(Config())
