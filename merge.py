import mp4_merger
import os
from audio import merge_audio_files

def get_folders_in_directory(directory):
    # List all entries in the directory and filter only folders
    folders = [os.path.join(directory,name) for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    # folders = [folder.replace("/","\\") for folder in folders]
    return folders

def delete_files(files):
    for file in files:
        os.remove(file)
        
def check_for_output_file(files):
    for file in files:
        if "output.MP4" in file:
            return True
    return False

def check_for_output_audio(files):
    for file in files:
        if "output.WAV" in file:
            return True
    return False

def renameFile(files,new_file):
    for old_file in files:
        if old_file.endswith(".MP4"):
            os.rename(old_file,new_file)
            
def renameAudioFile(files,new_file):
    for old_file in files:
        if old_file.endswith(".MP4"):
            os.rename(old_file,new_file)
    


def merge_file(folder,delete = False):
    files = os.listdir(folder)

    files = [os.path.join(folder, file) for file in files if file.endswith(".MP4")]
    
    # files = [file.replace("/","\\") for file in files]
    # files = ["G:\GoPro Vids\August 31, 2024 18_43\GX010019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX020019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX030019.MP4"]
    # print(files)
    if not check_for_output_file(files) and len(files) > 1:
        folder_name = folder.rsplit("\\",1)[1]
        output_file = f"{folder}\\{folder_name}.MP4"
        
        # output_file = output_file.replace("/","\\")
        # print(files)
        # print("Output File: ",output_file)
        try:
            mp4_merger.merge_videos(files, output_file)
            print("Videos merged successfully!")
            if delete:
                delete_files(files)
            return True
        except Exception as e:
            print(f"Error during merging: {e}")
            return False
    elif not check_for_output_file(files) and len(files) == 1:
        folder_name = folder.rsplit("\\",1)[1]
        output_file = f"{folder}\\{folder_name}.MP4"
        renameFile(files,output_file)
        return False
    
def merge_audio(folder,delete):
    files = os.listdir(folder)

    files = [os.path.join(folder, file) for file in files if file.endswith(".WAV")]
    
    # files = [file.replace("/","\\") for file in files]
    # files = ["G:\GoPro Vids\August 31, 2024 18_43\GX010019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX020019.MP4","G:\GoPro Vids\August 31, 2024 18_43\GX030019.MP4"]
    # print(files)
    if not check_for_output_audio(files) and len(files) > 1:
        folder_name = folder.rsplit("\\",1)[1]
        output_file = f"{folder}\\{folder_name}.WAV"
        
        try:
            merge_audio_files(files, output_file)
            print("Videos merged successfully!")
            if delete:
                delete_files(files)
            return True
        except Exception as e:
            print(f"Error during merging: {e}")
            return False
    elif not check_for_output_audio(files) and len(files) == 1:
        folder_name = folder.rsplit("\\",1)[1]
        output_file = f"{folder}\\{folder_name}.WAV"
        renameAudioFile(files,output_file)
        return False
            


def merge_files(FOLDER = "G:\GoPro Vids",delete = False):

    folders  = get_folders_in_directory(FOLDER)
    
    # print(folders)

    for i,folder in enumerate(folders):
        
        merge_file(folder,delete)
        merge_audio(folder,delete)
              
        print(f"{i+1}/{len(folders)} folders processed")