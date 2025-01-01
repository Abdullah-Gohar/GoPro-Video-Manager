import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from main import main, flatten_folder

# Create the main application window
root = tk.Tk()
root.title("GoPro Video Manager")
root.geometry("600x350")
root.config(bg="#2E2E2E")

global file_path

# Variables to manage the states of the checkboxes
folder_selected = False
merge_videos_var = tk.BooleanVar()
delete_clips_var = tk.BooleanVar()
flatten_var = tk.BooleanVar()

# Function to select folder path
def select_folder():
    global folder_selected
    folder_path = filedialog.askdirectory()
    global file_path
    file_path = folder_path
    if folder_path:
        folder_selected = True
        status_label.config(text="Folder Selected!", fg="#90EE90")  # Status update in green
        merge_checkbox.config(state=tk.NORMAL)
        flatten_checkbox.config(state=tk.NORMAL)
        run_button.config(state=tk.NORMAL)
    else:
        folder_selected = False
        status_label.config(text="No folder selected", fg="red")
        merge_checkbox.config(state=tk.DISABLED)
        flatten_checkbox.config(state=tk.DISABLED)
        delete_checkbox.config(state=tk.DISABLED)
        run_button.config(state=tk.DISABLED)

# Function to update the state of checkboxes
def toggle_merge():
    if merge_videos_var.get():
        delete_checkbox.config(state=tk.NORMAL)
        flatten_checkbox.config(state=tk.DISABLED)
    else:
        delete_checkbox.config(state=tk.DISABLED)
        flatten_checkbox.config(state=tk.NORMAL)
        
def toggle_flatten():
    if flatten_var.get():
        merge_checkbox.config(state=tk.DISABLED)
        delete_checkbox.config(state=tk.DISABLED)
    else:
        merge_checkbox.config(state=tk.NORMAL)

def run_process():
    if folder_selected:
        merge = merge_videos_var.get()
        delete = delete_clips_var.get()
        flatten_stat = flatten_var.get()

        status_label.config(text="Processing...", fg="#FFD700")  # Status update to indicate loading
        status_label.update_idletasks()  # Update the UI before long process
        root.update()  # Update the UI before long process

        # Simulate running the processes
        if flatten_stat:
            flatten_folder(file_path)
            messagebox.showinfo("Success", "Reverse Split Completed")
        else:
            main(file_path, merge, delete)
            messagebox.showinfo("Success", "Process Completed")
        
        status_label.config(text="Process Completed", fg="#90EE90")  # Update status on completion
    else:
        messagebox.showwarning("Error", "Please select a valid folder!")
        status_label.config(text="No folder selected", fg="red")

# Header label
header_label = tk.Label(root, text="GoPro Video Manager", font=("Arial", 18), bg="#2E2E2E", fg="white")
header_label.pack(pady=10)

# Button to select folder
folder_button = tk.Button(root, text="Select Folder", command=select_folder, font=("Arial", 12), bg="#4C4CFF", fg="white", width=20)
folder_button.pack(pady=10)

# Merge videos checkbox (disabled initially)
merge_checkbox = tk.Checkbutton(root, text="Merge videos", variable=merge_videos_var, command=toggle_merge, state=tk.DISABLED, bg="#2E2E2E", fg="white", selectcolor="#4C4CFF", font=("Arial", 12))
merge_checkbox.pack(pady=5)

# Delete clips checkbox (disabled initially)
delete_checkbox = tk.Checkbutton(root, text="Delete clips", variable=delete_clips_var, state=tk.DISABLED, bg="#2E2E2E", fg="white", selectcolor="#4C4CFF", font=("Arial", 12))
delete_checkbox.pack(pady=5)

# Reverse Split checkbox (disabled initially)
flatten_checkbox = tk.Checkbutton(root, text="Reverse Split", variable=flatten_var, command = toggle_flatten, state=tk.DISABLED, bg="#2E2E2E", fg="white", selectcolor="#4C4CFF", font=("Arial", 12))
flatten_checkbox.pack(pady=5)

# Run button (disabled initially)
run_button = tk.Button(root, text="Run", command=run_process, state=tk.DISABLED, font=("Arial", 12), bg="#4C4CFF", fg="white", width=15)
run_button.pack(pady=15)

# Status label to show dynamic status of the application
status_label = tk.Label(root, text="No folder selected", font=("Arial", 12), bg="#2E2E2E", fg="red")
status_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
