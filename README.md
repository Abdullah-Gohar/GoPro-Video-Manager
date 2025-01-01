# GoPro Video Manager

**GoPro Video Manager** is a tool designed to simplify the organization and management of GoPro video clips. The software renames traditional GoPro file names like `010134.mp4` into more human-readable formats, such as `November 16, 2024 06_55.MP4`, making it easier to browse, access, and edit your footage.

### Key Features
1. **File Renaming**: Converts GoPro's default file names into timestamp-based names.
2. **File Merging**: Combines GoPro's segmented video files into a single, high-quality clip, retaining all frames and quality.
3. **Audio Merging (Experimental)**: Merges external audio clips associated with video files, where applicable.
4. **File Restructuring**: Organizes clips into folders based on their capture date and time.

> **Note**:  
> The audio merging feature is still experimental, and renaming `.WAV` files associated with individual clips may not always work as intended.

---

## Download
To use the pre-built version of the manager, download the executable and necessary files from: [Download Link](https://www.mediafire.com/file/9omky6no7kkgzmy/GoPro+Video+Manager.zip/file).

---

## Installation and Setup

### Prerequisites
- **Python 3.7 or newer**
- **Rust**

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdullah-Gohar/GoPro-Video-Manager
   cd gopro-video-manager
   ```
2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```
3. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Build the `mp4_merger` library**:
   ```bash
   cd mp4_merger
   maturin develop
   cd ..
   ```
5. **Generate the executable**:
   ```bash
   python gen_installer.py
   ```
6. **Run the application directly**:
   ```bash
   python app.py
   ```

> **Note**: Ensure `exiftool_files` and `exiftool.exe` are in the same directory as the executable or the code for proper functionality.

---

## Software Guide

### Getting Started
1. Run the script using the instructions above.
2. Use the app interface to select the folder containing your GoPro exports.

### Main Functions
1. **Restructure Files**:  
   Groups all clips shot together into a single folder and renames them to the time and day of their original capture. This is the default behavior when a folder is selected and the "Run" button is clicked.

2. **Merge Files**:  
   When the "Merge Files" option is selected, the app groups clips as described above and merges multiple clips from a folder into a single video file.

3. **Delete Clips** (Optional):  
   An optional flag for merging. When enabled, all individual clips that were merged are deleted, leaving only the merged video file.

4. **Reverse Split**:  
   Reverts the default restructuring process. All files are pulled from their folders and placed into the root directory, retaining their timestamp-based names. Merged files remain merged.

---

## Contribution
Feel free to contribute to this project by:
- Submitting bug reports or feature requests.
- Forking the repository and making pull requests.

---

## License
[MIT License](LICENSE)  

--- 

**Happy organizing!** 🏞️
