import os
import csv
from app.config.configuration import Config

config = Config()
# Remove the file if it exists
file_name = "main_weekly_report.csv"
if os.path.exists(file_name):
    os.remove(file_name)

# Variables
focus_hours = 10
hard_wanted_hours = 85
no_mas = 4
exercise = 2
l_weight = 0.8
n_weight = 0.04
e_weight = 0.08
days = 7
exercise_times = 14

# Calculate scores
ultimate_score = (focus_hours / hard_wanted_hours) * l_weight + \
    (no_mas / days) * n_weight + \
    (exercise / exercise_times) * e_weight

ultimate_score = round(ultimate_score, 2)

learning_score = round(focus_hours / hard_wanted_hours, 2)
no_mas_core = round(no_mas / days, 2)
exercise_score = round(exercise / exercise_times, 2)

# Prepare data for CSV
doc = [
    ["", "percent", "score", "weight"],
    ["focus hours:", f"{focus_hours} | {hard_wanted_hours}", learning_score, l_weight],
    ["noMas:", f"{no_mas} | {days}", no_mas_core, n_weight],
    ["exercise:", f"{exercise} | {exercise_times}", exercise_score, e_weight],
    ["final:", "", "", f"{ultimate_score} (h)"]
]

# Write to CSV
with open(os.path.join(config.resource_dir, file_name), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(doc)

print(f"Report generated.: {file_name}")