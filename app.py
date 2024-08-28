import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

def count_lines_in_file(filepath):
    line_count = 0
    char_count = 0
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                char_count += len(line)
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
            for line in file:
                line_count += 1
                char_count += len(line)
    return line_count, char_count

def count_lines_in_folder(folder_path):
    file_lines = []
    total_lines = 0
    total_chars = 0

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                line_count, char_count = count_lines_in_file(file_path)
                relative_path = os.path.relpath(file_path, folder_path)
                file_lines.append((relative_path, line_count, char_count))
                total_lines += line_count
                total_chars += char_count

    # Sort the files by the number of lines in descending order
    file_lines.sort(key=lambda x: x[1], reverse=True)

    result = ""
    for relative_path, line_count, char_count in file_lines:
        result += f"{relative_path}: {line_count} lines, {char_count} characters\n"
    result += f"\nTotal lines in all files: {total_lines}\n"
    result += f"Total characters in all files: {total_chars}"
    
    return result

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        result = count_lines_in_folder(folder_path)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

def about():
    messagebox.showinfo("About", "Line Counter App\nVersion 1.0\nCreated by Dominic Minnich")

# Set up the main application window
root = tk.Tk()
root.title("Line Counter")
root.geometry("600x400")

# Add a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Add a frame for the browse button
frame = tk.Frame(root)
frame.pack(pady=10)

# Add a browse button
browse_button = tk.Button(frame, text="Browse Folder", command=browse_folder)
browse_button.pack()

# Add a scrolled text widget to display results
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
result_text.pack(pady=10)

# Start the application
root.mainloop()