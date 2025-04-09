import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os

# Excel file name
file_name = "mood_log.xlsx"

# Check if the file exists
if not os.path.exists(file_name):
    wb = Workbook()
    ws = wb.active
    ws.title = "Mood Log"
    ws.append(["Date", "Time", "Mood", "Reason"])
    wb.save(file_name)

# Ask user for mood and reason
mood = input("How are you feeling today? (happy/sad/tired/etc.): ")
reason = input("Why do you feel that way? (optional): ")

# Get current date and time
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

# Open the Excel file and add the entry
wb = openpyxl.load_workbook(file_name)
ws = wb.active
ws.append([date, time, mood, reason])
wb.save(file_name)

print("Mood saved successfully!")