import json
from utils import generate_folder_name_from_timestamp
import os
import shutil

def move_files(data):
    for path in data:
        files = data[path]
        folder_name = generate_folder_name_from_timestamp(path)
        base_path = files[0][0].rsplit("\\",1)[0]
        # print(base_path)
        folder_path = os.path.join(base_path,folder_name)
        os.makedirs(folder_path,exist_ok=True)
        
        for file in files:
            file_name = file[0].rsplit("\\",1)[1]
            without_ext = file_name.rsplit(".",1)[0]
            # print(os.listdir(base_path))
            for f in os.listdir(base_path):
                if without_ext in f and os.path.join(base_path,f) != folder_path:
                    print("Moving: ", os.path.join(base_path,f), " to ", os.path.join(folder_path,f))
                    shutil.move(os.path.join(base_path,f),os.path.join(folder_path,f))
            # print(file_name)
            # print(without_ext)
            
        # print(folder_name)
        # print(files)
        