import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

command = (
    f'pyinstaller --noconfirm --onefile --console --clean --name "GoPro Video Manager" '
    f'--hidden-import "tkinter" --hidden-import "pydub"  --hidden-import "mp4_merger" '
    # f'--add-data "{PROJECT_PATH}\\exiftool_files;exiftool_files/" '
    f'--add-data "{PROJECT_PATH}\\mp4_merger;mp4_merger/" '
    # f'--add-data "{PROJECT_PATH}\\exiftool.exe;." '
    f'--add-data "{PROJECT_PATH}\\main.py;." '
    f'--add-data "{PROJECT_PATH}\\merge.py;." '
    f'--add-data "{PROJECT_PATH}\\move.py;." '
    f'--add-data "{PROJECT_PATH}\\utils.py;." '
    # f'--add-data "{PROJECT_PATH}\\venv\\Lib\\site-packages\\pydub;pydub" '

    # '--add-binary "C:\\Program Files\\ffmpeg-7.1-essentials_build\\bin\\ffmpeg.exe;." '
    
    f'"{PROJECT_PATH}\\app.py"'
)

os.system(command)
