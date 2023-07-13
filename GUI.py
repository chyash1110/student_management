import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('academic_performance.db')
c = conn.cursor()

# Create a table for storing academic data if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS academic_data (
                roll_no INTEGER PRIMARY KEY,
                name TEXT,
                semester INTEGER,
                dob TEXT,
                sex TEXT,
                contact_no TEXT,
                subject1 INTEGER,
                subject2 INTEGER,
                subject3 INTEGER,
                subject4 INTEGER,
                subject5 INTEGER,
                subject6 INTEGER
            )''')
conn.commit()

# Function to store data in the database
def store_data():
    roll_no = int(roll_no_entry.get())
    name = name_entry.get()
    semester = int(semester_entry.get())
    dob = dob_entry.get()
    sex = sex_entry.get()
    contact_no = contact_no_entry.get()
    subject1 = int(subject1_entry.get())
    subject2 = int(subject2_entry.get())
    subject3 = int(subject3_entry.get())
    subject4 = int(subject4_entry.get())
    subject5 = int(subject5_entry.get())
    subject6 = int(subject6_entry.get())
    
    # Insert data into the table
    c.execute('''INSERT INTO academic_data (roll_no, name, semester, dob, sex, contact_no, subject1, subject2, subject3, subject4, subject5, subject6)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (roll_no, name, semester, dob, sex, contact_no, subject1, subject2, subject3, subject4, subject5, subject6))
    conn.commit()
    clear_entries()
    display_result("Data stored successfully!")

# Function to clear the entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    contact_no_entry.delete(0, tk.END)
    subject1_entry.delete(0, tk.END)
    subject2_entry.delete(0, tk.END)
    subject3_entry.delete(0, tk.END)
    subject4_entry.delete(0, tk.END)
    subject5_entry.delete(0, tk.END)
    subject6_entry.delete(0, tk.END)

# Function to display the result
def display_result(message):
    result_text.configure(state='normal')
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, message)
    result_text.configure(state='disabled')

# Function to search data by roll number
def search_by_roll_no():
    roll_no = int(roll_no_search_entry.get())
    c.execute('SELECT * FROM academic_data WHERE roll_no=?', (roll_no,))
    result = c.fetchone()
    if result:
        display_result(f"Roll No: {result[0]}\n"
                       f"Name: {result[1]}\n"
                       f"Semester: {result[2]}\n"
                       f"DOB: {result[3]}\n"
                       f"Sex: {result[4]}\n"
                       f"Contact No: {result[5]}\n"
                       f"Subject 1: {result[6]}\n"
                       f"Subject 2: {result[7]}\n"
                       f"Subject 3: {result[8]}\n"
                       f"Subject 4: {result[9]}\n"
                       f"Subject 5: {result[10]}\n"
                       f"Subject 6: {result[11]}")
    else:
        display_result("No data found for the given roll number.")

# Create the main window
window = tk.Tk()
window.title("Academic Performance Evaluation")

# Create labels and entry fields for input
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

semester_label = tk.Label(window, text="Semester:")
semester_label.pack()
semester_entry = tk.Entry(window)
semester_entry.pack()

roll_no_label = tk.Label(window, text="Roll No:")
roll_no_label.pack()
roll_no_entry = tk.Entry(window)
roll_no_entry.pack()

dob_label = tk.Label(window, text="DOB:")
dob_label.pack()
dob_entry = tk.Entry(window)
dob_entry.pack()

sex_label = tk.Label(window, text="Sex:")
sex_label.pack()
sex_entry = tk.Entry(window)
sex_entry.pack()

contact_no_label = tk.Label(window, text="Contact No:")
contact_no_label.pack()
contact_no_entry = tk.Entry(window)
contact_no_entry.pack()

subject1_label = tk.Label(window, text="Subject 1:")
subject1_label.pack()
subject1_entry = tk.Entry(window)
subject1_entry.pack()

subject2_label = tk.Label(window, text="Subject 2:")
subject2_label.pack()
subject2_entry = tk.Entry(window)
subject2_entry.pack()

subject3_label = tk.Label(window, text="Subject 3:")
subject3_label.pack()
subject3_entry = tk.Entry(window)
subject3_entry.pack()

subject4_label = tk.Label(window, text="Subject 4:")
subject4_label.pack()
subject4_entry = tk.Entry(window)
subject4_entry.pack()

subject5_label = tk.Label(window, text="Subject 5:")
subject5_label.pack()
subject5_entry = tk.Entry(window)
subject5_entry.pack()

subject6_label = tk.Label(window, text="Subject 6:")
subject6_label.pack()
subject6_entry = tk.Entry(window)
subject6_entry.pack()

# Create a button to store data
store_button = tk.Button(window, text="Store Data", command=store_data)
store_button.pack()

# Create labels and entry field for roll number search
roll_no_search_label = tk.Label(window, text="Search by Roll No:")
roll_no_search_label.pack()
roll_no_search_entry = tk.Entry(window)
roll_no_search_entry.pack()

# Create a button to search data
search_button = tk.Button(window, text="Search", command=search_by_roll_no)
search_button.pack()

# Create a text widget to display the result
result_text = tk.Text(window, height=10, width=50)
result_text.pack()
result_text.configure(state='disabled')

# Start the main event loop
window.mainloop()

# Close the database connection
conn.close()
