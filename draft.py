import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = firstEntry.get()
        lastname = secondEntry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
frame1 =tkinter.LabelFrame(frame, text="User Information")
frame1.grid(row= 0, column=0, padx=20, pady=10)

firstLabel = tkinter.Label(frame1, text="First Name")
firstLabel.grid(row=0, column=0)
secondLabel = tkinter.Label(frame1, text="Last Name")
secondLabel.grid(row=0, column=1)

firstEntry = tkinter.Entry(frame1)
secondEntry = tkinter.Entry(frame1)
firstEntry.grid(row=1, column=0)
secondEntry.grid(row=1, column=1)

title_label = tkinter.Label(frame1, text="Title")
title_combobox = ttk.Combobox(frame1, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(frame1, text="Age")
age_spinbox = tkinter.Spinbox(frame1, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(frame1, text="Nationality")
nationality_combobox = ttk.Combobox(frame1, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in frame1.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
frame2 = tkinter.LabelFrame(frame)
frame2.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(frame2, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(frame2, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(frame2, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(frame2, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(frame2, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(frame2, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in frame2.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()