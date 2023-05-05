# 1) using pip install tkinter 
#75% attendence 


def get_total_classes():
    while True:
        try:
            total_classes_held = int(input("Enter the total number of classes held: "))
            total_classes_attended = int(input("Enter the total number of classes attended: "))

            if total_classes_held <= 0 or total_classes_attended < 0 or total_classes_attended > total_classes_held:
                print("Invalid input. Please try again.")
                continue

            return total_classes_held, total_classes_attended

        except ValueError:
            print("Invalid input. Please try again.")

def calculate_attendance_percentage(total_classes_held, total_classes_attended):
    return (total_classes_attended / total_classes_held) * 100

def check_eligibility(attendance_percentage):
    if attendance_percentage < 75:
        print("Sorry, you cannot sit in the exam as your attendance percentage is less than 75%.")
    else:
        print("Congratulations, you are eligible to sit in the exam!")

total_classes_held, total_classes_attended = get_total_classes()
attendance_percentage = calculate_attendance_percentage(total_classes_held, total_classes_attended)
check_eligibility(attendance_percentage)









#2)python code to create a placement form

import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Placement Form")

# Define labels and entries for each field
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)

phone_label = tk.Label(root, text="Phone:")
phone_entry = tk.Entry(root)

college_label = tk.Label(root, text="College:")
college_entry = tk.Entry(root)

year_label = tk.Label(root, text="Year:")
year_entry = tk.Entry(root)

cgpa_label = tk.Label(root, text="CGPA:")
cgpa_entry = tk.Entry(root)

# Define a submit function to print the values entered
def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())
    print("Phone:", phone_entry.get())
    print("College:", college_entry.get())
    print("Year:", year_entry.get())
    print("CGPA:", cgpa_entry.get())

# Define a button to submit the form
submit_button = tk.Button(root, text="Submit", command=submit)

# Layout the labels, entries, and button using the grid manager
name_label.grid(row=0, column=0, sticky="E")
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0, sticky="E")
email_entry.grid(row=1, column=1)

phone_label.grid(row=2, column=0, sticky="E")
phone_entry.grid(row=2, column=1)

college_label.grid(row=3, column=0, sticky="E")
college_entry.grid(row=3, column=1)

year_label.grid(row=4, column=0, sticky="E")
year_entry.grid(row=4, column=1)

cgpa_label.grid(row=5, column=0, sticky="E")
cgpa_entry.grid(row=5, column=1)

submit_button.grid(row=6, column=1)

# Run the tkinter event loop
root.mainloop()








#3)create a set and perform 5 methods on it 


# Create a set of integers
my_set = {1, 2, 3, 4, 5}

# Print the set
print("Original Set:", my_set)

# Add an element to the set
my_set.add(6)
print("After Adding an Element:", my_set)

# Remove an element from the set
my_set.remove(3)
print("After Removing an Element:", my_set)

# Find the length of the set
print("Length of the Set:", len(my_set))

# Check if an element is in the set
if 4 in my_set:
    print("4 is in the Set")
else:
    print("4 is not in the Set")











#4)sports event registration form 

import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("Sports Event Registration Form")

# Create labels and input fields
name_label = tk.Label(window, text="Full Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_entry = tk.Entry(window)
gender_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

phone_label = tk.Label(window, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

event_label = tk.Label(window, text="Event:")
event_label.pack()
event_entry = tk.Entry(window)
event_entry.pack()

# Create a submit button
def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    event = event_entry.get()

    # Print the user's input
    print("Thank you for registering for the sports event!")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Email:", email)
    print("Phone Number:", phone)
    print("Event:", event)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Run the window
window.mainloop()










#5)Reverse number 

# Get the user input
number = int(input("Enter a number to reverse: "))

# Reverse the number using slicing
reverse = int(str(number)[::-1])

# Print the reversed number
print("The reversed number is:", reverse)











#6)python code to create all types of message box 


from tkinter import messagebox
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Show an info message box
messagebox.showinfo("Info", "This is an info message box.")

# Show a warning message box
messagebox.showwarning("Warning", "This is a warning message box.")

# Show an error message box
messagebox.showerror("Error", "This is an error message box.")

# Ask a yes/no question
answer = messagebox.askquestion("Question", "Do you want to proceed?")

# Print the user's answer
if answer == "yes":
    print("You clicked Yes.")
else:
    print("You clicked No.")

# Ask a yes/no/cancel question
answer = messagebox.askyesnocancel("Question", "Do you want to save changes?")

# Print the user's answer
if answer == True:
    print("You clicked Yes.")
elif answer == False:
    print("You clicked No.")
else:
    print("You clicked Cancel.")

# Show an input dialog box
answer = messagebox.askstring("Input", "Enter your name:")

# Print the user's input
if answer:
    print("Your name is:", answer)

# Show a file dialog box to open a file
file_path = messagebox.askopenfilename(title="Open File")

# Print the file path
if file_path:
    print("You selected the file:", file_path)

# Show a file dialog box to save a file
file_path = messagebox.asksaveasfilename(title="Save File")

# Print the file path
if file_path:
    print("You saved the file as:", file_path)














#7)python code for function that takes character adn returns true if it is not vowel 


def is_consonant(char):
    """
    Returns True if the input character is a consonant, False otherwise.
    """
    vowels = "aeiouAEIOU"
    if char.isalpha() and char not in vowels:
        return True
    else:
        return False

char = input("Enter a character: ")
if is_consonant(char):
    print(char, "is a consonant.")
else:
    print(char, "is a vowel.")












#8)python code to create event regristration form using widgets


from tkinter import *

# Create the main window
root = Tk()
root.title("Event Registration Form")

# Define the function to handle form submission
def submit_form():
    # Get user input
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    event = event_var.get()

    # Print the user's input
    print("Thank you for registering for the event!")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Email:", email)
    print("Phone Number:", phone)
    print("Event:", event)

    # Clear the form fields
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)

# Create form labels
name_label = Label(root, text="Name:")
age_label = Label(root, text="Age:")
gender_label = Label(root, text="Gender:")
email_label = Label(root, text="Email:")
phone_label = Label(root, text="Phone Number:")
event_label = Label(root, text="Event:")

# Create form entry fields
name_entry = Entry(root)
age_entry = Entry(root)
email_entry = Entry(root)
phone_entry = Entry(root)

# Create gender radio buttons
gender_var = StringVar()
male_button = Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_button = Radiobutton(root, text="Female", variable=gender_var, value="Female")
other_button = Radiobutton(root, text="Other", variable=gender_var, value="Other")

# Create event dropdown
event_var = StringVar()
event_var.set("Select an event...")
event_dropdown = OptionMenu(root, event_var, "Marathon", "Swimming Competition", "Basketball Tournament", "Chess Championship")

# Create submit button
submit_button = Button(root, text="Submit", command=submit_form)

# Add form elements to the window
name_label.grid(row=0, column=0, sticky=W)
name_entry.grid(row=0, column=1)
age_label.grid(row=1, column=0, sticky=W)
age_entry.grid(row=1, column=1)
gender_label.grid(row=2, column=0, sticky=W)
male_button.grid(row=2, column=1, sticky=W)
female_button.grid(row=2, column=2, sticky=W)
other_button.grid(row=2, column=3, sticky=W)
email_label.grid(row=3, column=0, sticky=W)
email_entry.grid(row=3, column=1)
phone_label.grid(row=4, column=0, sticky=W)
phone_entry.grid(row=4, column=1)
event_label.grid(row=5, column=0, sticky=W)
event_dropdown.grid(row=5, column=1)
submit_button.grid(row=6, column=1)

# Start the event loop
root.mainloop()

















#9)code that allows the user to input a list of integers and removes the 0th, 3rd, and 5th elements:


# Get user input
my_list = input("Enter a list of integers separated by commas: ").split(",")
my_list = [int(x.strip()) for x in my_list]

# Remove specified elements
del my_list[5]
del my_list[3]
del my_list[0]

# Print the modified list
print("Modified List:", my_list)

