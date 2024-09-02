import pandas as pd
from datetime import datetime, timedelta

# Sample data structure for timetable entries
# In a real application, this might be loaded from a database or other storage
timetable_entries = []

def add_entry(faculty_name, class_name, day, time):
    # Convert day and time to a datetime object for easier manipulation
    try:
        class_time = datetime.strptime(f"{day} {time}", "%A %H:%M")
    except ValueError:
        print("Invalid date or time format. Use 'Day HH:MM'.")
        return

    # Check for conflicts with existing entries
    for entry in timetable_entries:
        if entry['faculty_name'] == faculty_name and entry['day'] == day and entry['time'] == time:
            print("Conflict detected: This faculty already has a class at this time.")
            return
    
    # Add the new entry
    timetable_entries.append({
        'faculty_name': faculty_name,
        'class_name': class_name,
        'day': day,
        'time': time
    })
    print(f"Entry added: {faculty_name} - {class_name} on {day} at {time}")

def generate_timetable():
    # Create a DataFrame from the timetable entries
    df = pd.DataFrame(timetable_entries)
    
    # Group by day and sort by time
    df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.time
    df = df.sort_values(by=['day', 'time'])
    
    # Save the timetable to a CSV file
    df.to_csv('timetable.csv', index=False)
    print("Timetable generated and saved to 'timetable.csv'.")

if __name__ == "__main__":
    # Example usage
    add_entry("Dr. Smith", "Math 101", "Monday", "09:00")
    add_entry("Dr. Johnson", "Physics 202", "Monday", "11:00")
    add_entry("Dr. Smith", "Math 101", "Tuesday", "10:00")
    
    generate_timetable()
