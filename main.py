from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from db import Database
from librarian import LibrarianWindow
from student import StudentWindow



db = Database('library.db')

# Create window object
root = Tk()


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        # Set background image
        self.bg = ImageTk.PhotoImage(file="images/library2.gif")
        # Create canvas
        self.canvas = Canvas(root, width=700, height=700)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        # Add Text
        self.canvas.create_text(450, 40, text="Library Management", font=("Times 20 italic bold", 50,
                                                                          "underline", "bold"), fill="white")
        self.canvas.create_text(400, 250, text="Login As?", font=("Times", 35, "italic"), fill="white")
        self.canvas.create_text(750, 550, text="... browse the shelves", font=("Times", 25, "italic"), fill="white")
        # Create Buttons
        self.btn_img1 = PhotoImage(file="images/logo1.gif")
        self.btn_img2 = PhotoImage(file="images/logo2.gif")
        self.photo_img1 = self.btn_img1.subsample(2, 3)
        self.photo_img2 = self.btn_img2.subsample(2, 3)

        self.btn1 = Button(root, text="Librarian", font=("Times", 20, "bold"), image=self.photo_img1, width=100,
                           height=100, compound=TOP, command=self.librarian_window)
        self.btn1.place(x=300, y=300)
        self.btn2 = Button(root, text="Student", font=("Times", 20, "bold"), image=self.photo_img2, width=100,
                           height=100, compound=TOP, command=self.student_window)
        self.btn2.place(x=450, y=300)

    def librarian_window(self):
        self.lib_window = Toplevel(root)
        self.lib_window.title("Library Management")
        self.lib_window.geometry("500x400")
        self.lib_window.resizable(False, False)

        self.name1_var = StringVar()
        self.pass1_var = StringVar()

        label1 = Label(self.lib_window, text="Librarian", font=("Times", 35, "italic", "underline"))
        label1.pack(padx=30, pady=20)
        # Create Frame
        l_frame1 = Frame(self.lib_window, bd=5, relief=FLAT)
        l_frame1.place(x=65, y=60, width=300, height=300)
        # Create label and input field
        user_name1 = Label(l_frame1, text="Username:", font=("Andalus", 15, "bold"), bg="white")
        user_name1.place(x=60, y=60)
        user_name_entry1 = Entry(l_frame1, textvariable=self.name1_var, font=("times new roman", 15))
        user_name_entry1.place(x=60, y=80, width=200)

        password1 = Label(l_frame1, text="Password:", font=("Andalus", 15, "bold"), bg="white")
        password1.place(x=60, y=130)
        pass_entry1 = Entry(l_frame1, show="*", textvariable=self.pass1_var, font=("times new roman", 15))
        pass_entry1.place(x=60, y=150, width=200)
        # Create Buttons
        login_btn1 = Button(l_frame1, text="LOGIN", font=("Arial", 15, "bold"), bg="red",
                            command=self.librarian_login)
        login_btn1.place(x=60, y=200, width=200, height=40)
        prev_btn1 = Button(self.lib_window, text="Prev", font=("Times", 20, "bold"),
                           command=self.lib_window.destroy)
        prev_btn1.place(x=25, y=350)

    def student_window(self):
        self.stu_window = Toplevel(root)
        self.stu_window.title("Library Management")
        self.stu_window.geometry("500x400")
        self.stu_window.resizable(False, False)

        self.name2_var = StringVar()
        self.pass2_var = StringVar()

        label2 = Label(self.stu_window, text="Student", font=("Times", 35, "italic", "underline"))
        label2.pack(padx=30, pady=20)
        # Create Frame
        l_frame2 = Frame(self.stu_window, bd=5, relief=FLAT)
        l_frame2.place(x=65, y=60, width=300, height=300)
        # Create label and input field
        user_name2 = Label(l_frame2, text="Username:", font=("Andalus", 15, "bold"), bg="white")
        user_name2.place(x=60, y=60)
        user_name_entry2 = Entry(l_frame2, textvariable=self.name2_var, font=("times new roman", 15))
        user_name_entry2.place(x=60, y=80, width=200)

        password2 = Label(l_frame2, text="Password:", font=("Andalus", 15, "bold"), bg="white")
        password2.place(x=60, y=130)
        pass_entry2 = Entry(l_frame2, show="*", textvariable=self.pass2_var, font=("times new roman", 15))
        pass_entry2.place(x=60, y=150, width=200)
        # Create Buttons
        login_btn2 = Button(l_frame2, text="LOGIN", font=("Arial", 15, "bold"), bg="red",
                            command=self.student_login)
        login_btn2.place(x=60, y=200, width=200, height=40)
        prev_btn2 = Button(self.stu_window, text="Prev", font=("Times", 20, "bold"),
                           command=self.stu_window.destroy)
        prev_btn2.place(x=25, y=350)

    def librarian_login(self):
        # Fetch data from database
        conn = sqlite3.connect("library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM librarians WHERE username=? AND password=?",
                    (self.name1_var.get(), self.pass1_var.get()))
        row = cur.fetchone()
        if self.name1_var.get() == "" or self.pass1_var.get() == "":
            messagebox.showerror("Must fill up required fields!")
        elif row is None:
            messagebox.showerror("Invalid username or password!")
        else:
            messagebox.showinfo("Login successful!")
            self.lib_window.destroy()
            LibrarianWindow(root)
        # Clear Input fields
        self.name1_var.set("")
        self.pass1_var.set("")

    def student_login(self):
        # Fetch data from database
        conn = sqlite3.connect("library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE username=? AND password=?",
                    (self.name2_var.get(), self.pass2_var.get()))
        row = cur.fetchone()
        if self.name2_var.get() == "" or self.pass2_var.get() == "":
            messagebox.showerror("Must fill up required fields!")
        elif row is None:
            messagebox.showerror("Invalid username or password!")
        else:
            messagebox.showinfo("Login successful!")
            self.stu_window.destroy()
            StudentWindow(root)

        # Clear Input fields
        self.name2_var.set("")
        self.pass2_var.set("")


main = MainWindow(root)
root.mainloop()
