import subprocess
from datetime import datetime
# from moviepy.editor import VideoFileClip
import os
from collections import defaultdict
import shutil
from move import move_files
from merge import merge_files


def parse_creation_date(date_str):
    # print(date_str)
    # Extract the date and time part from the string (2024:09:06 17:59:49)
    # The date format is 'YYYY:MM:DD HH:MM:SS'
    date_part = date_str.split(": ", 1)[1].strip()

    # Convert to datetime object using the format 'YYYY:MM:DD HH:MM:SS'
    creation_datetime = datetime.strptime(date_part, '%Y:%m:%d %H:%M:%S')

    # Convert datetime object to the number of seconds since the epoch
    epoch_time = creation_datetime.timestamp()

    return epoch_time

def get_video_creation_time(file_path):
    # Run the ExifTool command to get all metadata
    result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capture the output from ExifTool
    output = result.stdout
    
    # Loop through each line to find the creation time (typically under "Create Date" or "Media Create Date")
    for line in output.splitlines():
        if "Create Date" in line or "Media Create Date" in line:
            # print(line)
            return line
    
    return "Creation date not found"

# def get_duration(file_path):
#     video = VideoFileClip(file_path)

#     # Get the duration in seconds
#     duration = video.duration
    
#     return duration



import os

def list_files_in_folder(folder_path):
    # Get a list of all files and directories in the folder
    all_files = os.listdir(folder_path)

    # Filter out directories to only include files
    files = [f for f in all_files if os.path.isfile(os.path.join(folder_path, f))]

    return files


def group_by_attribute(data, index):
    grouped = defaultdict(list)
    
    for item in data:
        key = item[index]
        grouped[key].append(item)
    
    return dict(grouped)



def flatten_folder(root_folder):
    # Walk through the root folder
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # If we're not in the root folder, move files to the root folder
        if dirpath != root_folder:
            for file in filenames:
                # Construct full file path
                file_path = os.path.join(dirpath, file)
                # Move the file to the root folder
                shutil.move(file_path, root_folder)

    # Remove empty subfolders
    for dirpath, dirnames, filenames in os.walk(root_folder, topdown=False):
        # If the directory is not the root folder and it's empty, remove it
        if dirpath != root_folder and not os.listdir(dirpath):
            os.rmdir(dirpath)
            
            
def parse_file(file_path):
    import traceback
    if not file_path.endswith(".MP4"):
        return 0
        # print(file_path)
    try:
        creation_date = get_video_creation_time(file_path)
        epoch = parse_creation_date(creation_date)
        creation_date = creation_date.split(": ",1)[1].strip()
        
        
    except:
        print(traceback.format_exc())
        return None
        
    return [file_path,creation_date,epoch]

def get_parsing_paths(PATH):
    files = list_files_in_folder(PATH)
    files  = [os.path.join(PATH, file) for file in files]
    
    return files

def sort_data(creation_dates):
    creation_dates.sort(key=lambda x: x[1])

        
    creation_dates = group_by_attribute(creation_dates, 1)
    
    return creation_dates

def parse_files(PATH):
    files = get_parsing_paths(PATH)
    creation_dates = []
    i = 1
    length = len([file for file in files if file.endswith(".MP4")])
    for file_path in files:
        data = parse_file(file_path)
        if data:
            creation_dates.append(data)
            
            print(f"{i}/{length} files processed")
            i += 1
        


    creation_dates = sort_data(creation_dates)
    
    return creation_dates

def main(PATH, merge_status = False, delete = False):
    
    date_data = parse_files(PATH)
    move_files(date_data)
    
    if merge_status:
        merge_files(PATH,delete)


# if __name__ == "__main__":
#     # main("G:\GoPro Vids", merge_status=True, delete=True)
#     main("G:\GoPro Vids - Copy", merge_status=False, delete=False)