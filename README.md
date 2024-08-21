# Line Counter App

## Overview

The Line Counter App is a simple Python application that allows you to count the number of lines in all text files within a selected folder. The application provides a graphical user interface (GUI) using Tkinter, making it easy for users to browse folders and view the results.
(Warning: This does count png, gif... and will add those lines to your count.)

![image](https://github.com/user-attachments/assets/4adbb82f-eb24-4f3f-99a7-13d6fbb4f0d6)


## Features

- **Browse and Select Folder:** The application allows users to browse and select a folder from their file system.
- **Line Counting:** The app counts the number of lines in each text file within the selected folder, including subfolders.
- **Results Display:** The results, including the number of lines per file and the total lines in all files, are displayed in a scrollable text area.
- **Sorting:** Files are sorted by the number of lines in descending order.
- **About Section:** The app includes an "About" dialog box that provides information about the application.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/line-counter-app.git
   cd line-counter-app
Install Dependencies:
This application only requires Python's standard libraries (os, tkinter). If you don't have Tkinter installed, you can install it using the following command (for Debian-based Linux distributions):

bash
Copy code
sudo apt-get install python3-tk
Run the Application:

bash
Copy code
python3 line_counter.py
Usage
Start the Application:
Run the script using Python. A GUI window will appear.

Browse Folder:
Click the "Browse Folder" button to open a file dialog. Select the folder containing the files you want to analyze.

View Results:
After selecting a folder, the application will display the number of lines for each file in the folder, sorted by line count. The total number of lines across all files will also be shown.

About:
You can view information about the application by clicking on the "Help" menu and selecting "About."
