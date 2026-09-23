# Problem Statement: Exam Seat Arrangement Maker


# 1. Project Name
Exam Seat Arrangement Maker


# 2. The Problem
In schools and colleges, arranging exam seats by hand takes a lot of time and effort. Teachers have to count available desks, write roll numbers, and make charts manually.
Doing this by hand causes a few common problems:
i) Mistakes happen easily: Teachers might write the same roll number twice or miss a student
ii) Cheating: When students sit in their normal roll number order, it is easy to cheat from friends sitting nearby.
iii) Seat counting issues: It is hard to quickly check if the total desks in all rooms are enough for all students
iv) Repeated work: For every new exam, teachers have to make the whole seating chart from scratch again.


# 3. My Solution
The Exam Seat Arrangement Maker is a simple Python program that makes exam seating plans automatically[cite: 1, 7, 8].
You just enter student details and room sizes . The program randomly shuffles the roll numbers so students get mixed up, then assigns each student to a desk. Extra desks are marked as `"empty"`, and if rooms run out of space, the program tells you which students are left without a seat.


# 4. Main Goals
i) Random Seating: Mix up student roll numbers using `random.shuffle()` so students cannot predict their seats
ii) Simple Room Layouts: Set up rooms as rows and columns, just like real classrooms
iii) Save and Reuse Data: Save students and rooms in simple text files (`students.txt` and `rooms.txt`) so you don't have to type them in every time
iv) Show and Save Results: Print the final seating chart on the screen and save it into `seatingoutput.txt`
v) Check for Simple Errors: Show a clear warning if a duplicate roll number or duplicate room name is entered.


# 5. Scope & Future Plans
a) What it does now:
  i) Handles multiple exam rooms of different sizes.
  ii) Uses a simple text-based menu (Enter new data, use saved data, or exit)
  iii) Runs using basic Python without installing any extra software
b) What can be added later:
  i) A friendly graphical window (GUI) instead of the black terminal screen.
  ii) An option to make sure two students from the same branch never sit right next to each other.