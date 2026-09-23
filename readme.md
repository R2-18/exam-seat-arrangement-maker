# Exam Seat Arrangement Maker

A modular, menu-driven Python project made to automate student exam seating arrangements across multiple rooms


## 1. Project Overview

The Exam Seat Arrangement Maker helps exam coordinators organize seating plans quickly.

Instead of arranging students manually, this program takes student roll numbers and room sizes, shuffles the students randomly and assigns each student to a specific row and seat. If extra seats remain in a room, they are marked as empty. If there are more students than the available seats can accommodate, the program warns the user and lists the remaining unallocated students.

## 2. Features

- Modular Code: Divided into four separate files to keep the code organized and easy to maintain.
- Fair Allocation: Uses Python's built-in `random.shuffle()` to ensure completely unbiased seat assignments.
- Duplicate Checking: Flags duplicate roll numbers and duplicate room names to prevent errors.
- Dual Output: Displays the final seating plan directly on the terminal screen and saves a copy to `seatingoutput.txt`.
- File Handling: Stores student and room records in simple text files (`students.txt` and `rooms.txt`) without requiring any external databases.

## 3. Project File Structure

Project vityarthi exam seat arrangement maker

1. setup_files.py       # Takes student and room input and writes them to text files
2. reader.py            # Reads and checks data from text files
3. allocator.py         # Shuffles roll numbers and assigns seats room by room
4. main.py              # Main menu, console display, and output file generation
5. students.txt         # Saved student records (Roll, Name, Branch)
6. rooms.txt            # Saved room records (Room Name, Rows, Columns)
7. seatingoutput.txt    # Generated final seating chart with seat numbers

## 4. Module Descriptions
a) setup_files.py
Handles user input and writes raw data to disk:  
-----stddata(): Asks for student roll numbers, names, and branches, then saves them to students.txt.  
-----roomdata(): Asks for room names, row counts, and column counts, then saves them to rooms.txt.  
-----newdata(): Runs both input functions in order.

b) reader.py
Reads data from the saved text files safely:  
-----fileexist(): Checks if both students.txt and rooms.txt exist before trying to read them. 
-----readstd(): Reads student details, skips empty lines, avoids duplicate roll numbers, and returns a list of roll numbers alongside a details dictionary.   -----readroom(): Reads room details and converts rows and columns into integers.  

c) allocator.py
Contains the core logic for seat assignments:  
-----allocate(rnolist, roomnos): Creates a copy of the student list, shuffles it randomly, and places students into room grids based on rows and columns.       -----Unoccupied seats receive "empty", and any leftover students are returned in leftseat.   

  
d) main.py
The main driver script of the project:   
-----Displays a console menu with options to use saved files, enter new records, or exit.  
-----dsresults(): Formats the final arrangement into clearly labeled rows and seat numbers, prints the chart on screen, and writes it to seatingoutput.txt.   

## 5. Steps to run this project
step-1----open the folder in terminal
step-2----type in "python main.py"
step-3---- !! YOU ARE IN !! proceed with the menu
