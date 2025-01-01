from datetime import datetime
import calendar
import re

def sanitize_folder_name(name):
    # Replace invalid characters with underscores
    name = re.sub(r'[\/:*?"<>|]', '_', name)
    # Trim leading and trailing spaces
    name = name.strip()
    return name

def generate_folder_name_from_timestamp(timestamp):
    input_format = '%Y:%m:%d %H:%M:%S'
    
    try:
        # Parse the timestamp string into a datetime object
        dt = datetime.strptime(timestamp, input_format)
        
        # Format the datetime object into a readable folder name
        month_name = calendar.month_name[dt.month]  # Get the full month name
        folder_name = f"{month_name} {dt.day:02d}, {dt.year} {dt.hour:02d}_{dt.minute:02d}"
        
        # Sanitize the folder name
        return sanitize_folder_name(folder_name)
    except ValueError:
        return "Invalid timestamp format"

# Example usage
# timestamp = "2024:08:07 20:32:23"
# folder_name = generate_folder_name_from_timestamp(timestamp)
# print(f"Folder Name: {folder_name}")
