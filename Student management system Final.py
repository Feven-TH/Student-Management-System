import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, id, name, dob, contact, email):
        self.id = id
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}, Contact: {self.contact}, Email: {self.email}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def search_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def register_student(self, id, name, dob, contact, email):
        student = Student(id, name, dob, contact, email)
        self.students.append(student)
        return "New student is successfully registered"

    def bubble_sort_students(self):
        n = len(self.students)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if self.students[j].name > self.students[j + 1].name:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]
                    swapped = True
            if not swapped:
                break
        return "Students sorted by name you can display to check."

    def display_students(self):
        if not self.students:
            return "No students registered."
        return "\n".join(str(student) for student in self.students)

    def update_student(self, id, name=None, contact=None, email=None):
        for student in self.students:
            if student.id == id:
                if name:
                    student.name = name
                if contact:
                    student.contact = contact
                if email:
                    student.email = email
                return "Student updated successfully"
        return "Student not found"

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

class StudentManagementGUI:
    def __init__(self, root, system):
        self.system = system
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("500x500")  # Setting initial size of the window
        self.root.config(bg="lightgrey")  # Adding background color to the window

        # Main Menu Frame
        self.main_menu_frame = tk.Frame(root, bg="lightgrey", padx=20, pady=20)  # Adding background color and padding
        self.main_menu_frame.pack()

        tk.Button(self.main_menu_frame, text="Register Student", command=self.show_register_frame, bg="Blue", fg="white").pack(pady=20)
        tk.Button(self.main_menu_frame, text="Search Student", command=self.show_search_frame, bg="Green", fg="white").pack(pady=15)
        tk.Button(self.main_menu_frame, text="Update Student", command=self.show_update_frame, bg="Red", fg="white").pack(pady=15)
        tk.Button(self.main_menu_frame, text="Sort Students", command=self.sort_students, bg="Orange", fg="white").pack(pady=15)
        tk.Button(self.main_menu_frame, text="Display Students", command=self.show_display_frame, bg="Brown", fg="white").pack(pady=15)
        tk.Button(self.main_menu_frame, text="Delete Student", command=self.show_delete_frame, bg="Purple", fg="white").pack(pady=15)

        # Register Section
        self.register_frame = tk.Frame(root, bg="#ADD8E6")

        tk.Label(self.register_frame, text="ID").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.register_frame, text="Name").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.register_frame, text="DOB (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.register_frame, text="Contact").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.register_frame, text="Email").grid(row=4, column=0, padx=10, pady=10)

        self.id_entry = tk.Entry(self.register_frame)
        self.name_entry = tk.Entry(self.register_frame)
        self.dob_entry = tk.Entry(self.register_frame)
        self.contact_entry = tk.Entry(self.register_frame)
        self.email_entry = tk.Entry(self.register_frame)

        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.dob_entry.grid(row=2, column=1, padx=10, pady=10)
        self.contact_entry.grid(row=3, column=1, padx=10, pady=10)
        self.email_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.register_frame, text="Register", command=self.register_student).grid(row=5, columnspan=2, padx=10, pady=10)
        tk.Button(self.register_frame, text="Back", command=self.show_main_menu).grid(row=6, columnspan=2, padx=10, pady=10)

        # Display Section
        self.display_frame = tk.Frame(root, bg="#90EE90")
        self.display_text = tk.Text(self.display_frame, height=10, width=50)
        self.display_text.pack()
        tk.Button(self.display_frame, text="Display", command=self.display_students).pack()
        tk.Button(self.display_frame, text="Back", command=self.show_main_menu).pack()

        # Search Section
        self.search_frame = tk.Frame(root, bg="#D2B48C")
        tk.Label(self.search_frame, text="ID").grid(row=0, column=0, padx=10, pady=10)
        self.search_id_entry = tk.Entry(self.search_frame)
        self.search_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.search_frame, text="Search", command=self.search_student).grid(row=1, columnspan=2, padx=10, pady=10)
        self.search_result = tk.Label(self.search_frame, text="")
        self.search_result.grid(row=2, columnspan=2, padx=10, pady=10)
        tk.Button(self.search_frame, text="Back", command=self.show_main_menu).grid(row=3, columnspan=2, padx=10, pady=10)

        # Update Section
        self.update_frame = tk.Frame(root, bg="#FFD700")
        tk.Label(self.update_frame, text="ID").grid(row=0, column=0, padx=10, pady=10)
        self.update_id_entry = tk.Entry(self.update_frame)
        self.update_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.update_frame, text="New Name").grid(row=1, column=0, padx=10, pady=10)
        self.update_name_entry = tk.Entry(self.update_frame)
        self.update_name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.update_frame, text="New Contact").grid(row=2, column=0, padx=10, pady=10)
        self.update_contact_entry = tk.Entry(self.update_frame)
        self.update_contact_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.update_frame, text="New Email").grid(row=3, column=0, padx=10, pady=10)
        self.update_email_entry = tk.Entry(self.update_frame)
        self.update_email_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.update_frame, text="Update", command=self.update_student).grid(row=4, columnspan=2, padx=10, pady=10)
        tk.Button(self.update_frame, text="Back", command=self.show_main_menu).grid(row=5, columnspan=2, padx=10, pady=10)

        # Delete Section
        self.delete_frame = tk.Frame(root, bg="#FF6347")
        tk.Label(self.delete_frame, text="ID").grid(row=0, column=0, padx=10, pady=10)
        self.delete_id_entry = tk.Entry(self.delete_frame)
        self.delete_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.delete_frame, text="Delete", command=self.delete_student).grid(row=1, columnspan=2, padx=10, pady=10)
        tk.Button(self.delete_frame, text="Back", command=self.show_main_menu).grid(row=2, columnspan=2, padx=10, pady=10)

    def show_main_menu(self):
        self.hide_all_frames()
        self.main_menu_frame.pack()

    def hide_all_frames(self):
        self.main_menu_frame.pack_forget()
        self.register_frame.pack_forget()
        self.display_frame.pack_forget()
        self.search_frame.pack_forget()
        self.update_frame.pack_forget()
        self.delete_frame.pack_forget()

    def show_register_frame(self):
        self.hide_all_frames()
        self.register_frame.pack()

    def show_display_frame(self):
        self.hide_all_frames()
        self.display_frame.pack()

    def show_search_frame(self):
        self.hide_all_frames()
        self.search_frame.pack()

    def show_update_frame(self):
        self.hide_all_frames()
        self.update_frame.pack()

    def show_delete_frame(self):
        self.hide_all_frames()
        self.delete_frame.pack()

    def register_student(self):
        try:
            id = int(self.id_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for ID.")
            return
        try:
            contact = int(self.contact_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for Contact.")
            return
        
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        email = self.email_entry.get()
        message = self.system.register_student(id, name, dob, contact, email)
        messagebox.showinfo("Register", message)
        self.show_main_menu()

    def display_students(self):
        students = self.system.display_students()
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, students)

    def search_student(self):
        try:
            id = int(self.search_id_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for ID.")
            return
        
        student = self.system.search_student(id)
        if student:
            self.search_result.config(text=str(student))
        else:
            self.search_result.config(text="Student not found")

    def update_student(self):
        try:
            id = int(self.update_id_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for ID.")
            return
        
        contact = self.update_contact_entry.get()
        if contact:
            try:
                contact = int(contact)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid integer for Contact.")
                return
        else:
            contact = None
        
        name = self.update_name_entry.get() or None
        email = self.update_email_entry.get() or None
        message = self.system.update_student(id, name, contact, email)
        messagebox.showinfo("Update", message)

    def delete_student(self):
        try:
            id = int(self.delete_id_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for ID.")
            return
        
        message = self.system.delete_student(id)
        messagebox.showinfo("Delete", message)

    def sort_students(self):
        message = self.system.bubble_sort_students()
        messagebox.showinfo("Sort", message)

if __name__ == "__main__":
    root = tk.Tk()
    system = StudentManagementSystem()
    sample_data=[
        {'id':'001','name':'Abebe','dob':'1999-6-3','contact':'0913685478','email':'abebe45@gmail.com'},
        {'id':'004','name':'Zebiba','dob':'2004-9-2','contact':'0929681850','email':'zebib22@gmail.com'},
        {'id':'002','name':'Almaz','dob':'1994-8-13','contact':'0911688475','email':'almaz65@gmail.com'},
        {'id':'003','name':'Hirut','dob':'2003-1-9','contact':'0906681958','email':'hirutH16@gmail.com'},
    ]

    for data in sample_data:
        system.register_student(data['id'], data['name'], data['dob'], data['contact'], data['email'])
    app = StudentManagementGUI(root, system)
    root.mainloop()
