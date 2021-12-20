import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, StringVar
from tkcalendar import *




class StudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("950x600")
        self.root.resizable(False, False)
        # Create book table
        data_frame = Frame(root)
        data_frame.place(x=420, y=90, width=500, height=408)

        search_frame = Frame(data_frame, bg="lightgray", bd=5, relief=FLAT)
        search_frame.pack(side=TOP, fill=X)

        display_frame = Frame(data_frame, bd=5, relief=GROOVE)
        display_frame.pack(fill=BOTH, expand=True)

        command_frame = LabelFrame(root, text="Commands", font=("Times italic bold", 16), relief=GROOVE)
        command_frame.place(x=170, y=502, width=500, height=80)

        issued_frame = LabelFrame(root, text="Issued Book", font=("Times italic bold", 16), relief=GROOVE)
        issued_frame.place(x=20, y=90, width=385, height=200)

        return_frame = LabelFrame(root, text="Returned Info", font=("Times italic bold", 16), relief=GROOVE)
        return_frame.place(x=20, y=300, width=385, height=200)

        # Create logout button
        logout_btn = Button(root, text='Logout', font=("Arial bold", 15), fg='red', width=8, command=self.logout)
        logout_btn.place(x=850, y=50)

        # Text Variables
        self.search = StringVar()

        # Create search button
        search_btn = Button(search_frame, text="Search", font=("Arial bold", 16), bg="lightgray", width=10,
                            command=self.search_item)
        search_btn.grid(row=0, column=0, pady=2)
        search_entry = Entry(search_frame, width=12, textvariable=self.search)
        search_entry.grid(row=0, column=1, padx=5, pady=2)
        self.search_by = ttk.Combobox(search_frame, value=["ISBN", "Title", "Publisher"], font=("Arial", 14), width=12)
        self.search_by.current(0)
        self.search_by.grid(row=0, column=2, pady=2)
        showall_btn = Button(search_frame, text="Show all", font=("Arial bold", 16), bg="lightgray",
                             width=10, command=self.populate_list)
        showall_btn.grid(row=0, column=4, padx=16, pady=10)

        # Add column heading and scroll bars
        y_scroll = Scrollbar(display_frame, orient=VERTICAL)
        x_scroll = Scrollbar(display_frame, orient=HORIZONTAL)

        self.book_table = ttk.Treeview(display_frame, columns=("SN", "ISBN", "TITLE", "GENRE", "AUTHOR FIRST NAME",
                                                               "AUTHOR LAST NAME", "PUBLISHER", "CATEGORIES",
                                                               "DESCRIPTION"),
                                       yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        y_scroll.config(command=self.book_table.yview)
        x_scroll.config(command=self.book_table.xview)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.pack(side=BOTTOM, fill=X)

        # Create table headings
        self.book_table.heading("SN", text="SN")
        self.book_table.heading("ISBN", text="ISBN")
        self.book_table.heading("TITLE", text="TITLE")
        self.book_table.heading("GENRE", text="GENRE")
        self.book_table.heading("AUTHOR FIRST NAME", text="AUTHOR FIRST NAME")
        self.book_table.heading("AUTHOR LAST NAME", text="AUTHOR LAST NAME")
        self.book_table.heading("PUBLISHER", text="PUBLISHER")
        self.book_table.heading("CATEGORIES", text="CATEGORIES")
        self.book_table.heading("DESCRIPTION", text="DESCRIPTION")
        self.book_table["show"] = "headings"

        # Adjust column headings
        self.book_table.column("SN", width=50, anchor=CENTER)
        self.book_table.column("ISBN", width=150, anchor=CENTER)
        self.book_table.column("TITLE", width=150, anchor=CENTER)
        self.book_table.column("GENRE", width=150, anchor=CENTER)
        self.book_table.column("AUTHOR FIRST NAME", width=200, anchor=CENTER)
        self.book_table.column("AUTHOR LAST NAME", width=200, anchor=CENTER)
        self.book_table.column("PUBLISHER", width=200, anchor=CENTER)
        self.book_table.column("CATEGORIES", width=100, anchor=CENTER)
        self.book_table.column("DESCRIPTION", width=200, anchor=CENTER)

        # Create buttons
        add_btn = Button(command_frame, text='Issue Book', font=("Arial bold", 15),
                         width=12, command=self.issue_page, padx=3)
        add_btn.grid(row=0, column=0, padx=20, pady=20)
        remove_btn = Button(command_frame, text='Return Book', font=("Arial bold", 15),
                            width=12, command=self.return_page)
        remove_btn.grid(row=0, column=1, padx=20)
        remove_btn = Button(command_frame, text='Remove Book', font=("Arial bold", 15),
                            width=12, command=self.remove_page)
        remove_btn.grid(row=0, column=2, padx=20)
        self.book_table.pack(fill=BOTH, expand=True)

        # Create table for issued book
        y_scroll = Scrollbar(issued_frame, orient=VERTICAL)
        x_scroll = Scrollbar(issued_frame, orient=HORIZONTAL)

        self.issued_table = ttk.Treeview(issued_frame,
                                         columns=("SN", "BOOK ISBN", "BOOK TITLE", "LIBRARY CARD", "STUDENT NAME",
                                                  "ISSUED DATE", "DUE DATE"),
                                         yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        y_scroll.config(command=self.issued_table.yview)
        x_scroll.config(command=self.issued_table.xview)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.pack(side=BOTTOM, fill=X)

        # Create table headings
        self.issued_table.heading("SN", text="SN")
        self.issued_table.heading("BOOK ISBN", text="BOOK ISBN")
        self.issued_table.heading("BOOK TITLE", text="BOOK TITLE")
        self.issued_table.heading("LIBRARY CARD", text="LIBRARY CARD")
        self.issued_table.heading("STUDENT NAME", text="STUDENT NAME")
        self.issued_table.heading("ISSUED DATE", text="ISSUED DATE")
        self.issued_table.heading("DUE DATE", text="DUE DATE")
        self.issued_table["show"] = "headings"
        # Adjust column headings
        self.issued_table.column("SN", width=50, anchor=CENTER)
        self.issued_table.column("BOOK ISBN", width=150, anchor=CENTER)
        self.issued_table.column("BOOK TITLE", width=150, anchor=CENTER)
        self.issued_table.column("LIBRARY CARD", width=150, anchor=CENTER)
        self.issued_table.column("STUDENT NAME", width=150, anchor=CENTER)
        self.issued_table.column("ISSUED DATE", width=150, anchor=CENTER)
        self.issued_table.column("DUE DATE", width=150, anchor=CENTER)
        self.issued_table.pack(fill=BOTH, expand=True)

        # Create label for return info
        self.stu_name_label = Label(return_frame, text="Student Name:", font=("Arial bold", 15), pady=2)
        self.stu_name_label.grid(row=0, column=0, sticky=W)
        self.stu_name_entry = Label(return_frame, text="")
        self.stu_name_entry.grid(row=0, column=1, sticky=W)

        self.bk_title_label = Label(return_frame, text="Book's Title:", font=("Arial bold", 15), pady=2)
        self.bk_title_label.grid(row=1, column=0, sticky=W)
        self.bk_title_entry = Label(return_frame, text="")
        self.bk_title_entry.grid(row=1, column=1, sticky=W)

        self.iss_date_label = Label(return_frame, text="Issued Date:", font=("Arial bold", 15), pady=2)
        self.iss_date_label.grid(row=2, column=0, sticky=W)
        self.iss_date_entry = Label(return_frame, text="")
        self.iss_date_entry.grid(row=2, column=1, sticky=W)

        self.due_date_label = Label(return_frame, text="Due Date:", font=("Arial bold", 15), pady=2)
        self.due_date_label.grid(row=3, column=0, sticky=W)
        self.due_date_entry = Label(return_frame, text="")
        self.due_date_entry.grid(row=3, column=1, sticky=W)

        self.rtn_date_label = Label(return_frame, text="Returned Date:", font=("Arial bold", 15), pady=2)
        self.rtn_date_label.grid(row=4, column=0, sticky=W)
        self.rtn_date_entry = Label(return_frame, text="")
        self.rtn_date_entry.grid(row=4, column=1, sticky=W)

        self.fine_label_entry = Label(return_frame, text="", font=("Times 20 italic bold", 15))
        self.fine_label_entry.grid(row=5, column=1)

        self.populate_list()
        self.fetch_issued()

    def search_item(self):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        selected = self.search_by.get()
        searched = self.search.get()
        if selected == "ISBN":
            self.query = "SELECT * FROM books WHERE isbn LIKE ?"
        if selected == "Title":
            self.query = "SELECT * FROM books WHERE title LIKE ?"
        if selected == "Publisher":
            self.query = "SELECT * FROM books WHERE publisher LIKE ?"

        name = (searched,)
        cur.execute(self.query, name)
        results = cur.fetchall()
        if len(results) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for result in results:
                self.book_table.insert('', END, values=result)
            conn.commit()
        conn.close()
        self.search.set("")

    def populate_list(self):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for row in rows:
                self.book_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def fetch_issued(self):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM issue_books")
        results = cur.fetchall()
        if len(results) != 0:
            self.issued_table.delete(*self.issued_table.get_children())
            for row in results:
                self.issued_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def issue_page(self):
        self.issue_window = Toplevel(self.root)
        self.issue_window.title("Library Management")
        self.issue_window.geometry("500x400")
        self.issue_window.resizable(False, False)
        self.issue_window.configure(bg="azure")
        # Create Text Variables
        self.book_isbn_text = StringVar()
        self.book_title_text = StringVar()
        self.library_card_text = StringVar()
        self.student_name_text = StringVar()
        self.issue_date_text = StringVar()
        self.return_date_text = StringVar()
        # Create title
        title = Label(self.issue_window, text="Issue Books!", font=("Times 20 italic bold", 30, "underline", "bold"))
        title.place(x=150, y=20)
        # Create buttons
        exit_btn = Button(self.issue_window, text="Exit", font="Times 20 italic bold",
                          command=self.issue_window.destroy)
        exit_btn.place(x=250, y=355)
        # Create frame
        issue_frame = LabelFrame(self.issue_window, text="Details", font=("Times italic bold", 16), relief=GROOVE)
        issue_frame.place(x=20, y=70, width=460, height=280)
        # Create labels
        library_card = Label(issue_frame, text="Library Card No.", font="Times 20 italic bold")
        library_card.grid(row=0, column=0, padx=30, pady=3)
        library_card_entry = Entry(issue_frame, textvariable=self.library_card_text, width=16)
        library_card_entry.grid(row=1, column=0, padx=30, pady=3)

        student_name = Label(issue_frame, text="Student Name", font="Times 20 italic bold")
        student_name.grid(row=0, column=1, padx=30, pady=3)
        student_name_entry = Entry(issue_frame, textvariable=self.student_name_text, width=16)
        student_name_entry.grid(row=1, column=1, padx=30, pady=3)

        book_isbn = Label(issue_frame, text="Book ISBN", font="Times 20 italic bold")
        book_isbn.grid(row=2, column=0, padx=30, pady=3)
        book_isbn_entry = Entry(issue_frame, textvariable=self.book_isbn_text, width=16)
        book_isbn_entry.grid(row=3, column=0, padx=30, pady=3)

        book_title = Label(issue_frame, text="Book Title", font="Times 20 italic bold")
        book_title.grid(row=2, column=1, padx=30, pady=3)
        book_title_entry = Entry(issue_frame, textvariable=self.book_title_text, width=16)
        book_title_entry.grid(row=3, column=1, padx=30, pady=3)

        issue_date = Label(issue_frame, text="Issue Date", font="Times 20 italic bold")
        issue_date.grid(row=4, column=0, padx=30, pady=3)
        issue_date_entry = DateEntry(issue_frame, textvariable=self.issue_date_text, width=16)
        issue_date_entry.grid(row=5, column=0, padx=30, pady=3)

        return_date = Label(issue_frame, text="Return Due Date", font="Times 20 italic bold")
        return_date.grid(row=4, column=1, padx=30, pady=3)
        return_date_entry = DateEntry(issue_frame, textvariable=self.return_date_text, width=16)
        return_date_entry.grid(row=5, column=1, padx=30, pady=3)

        submit_btn = Button(self.issue_window, text="Issue", font="Times 20 italic bold", command=self.issue_book)
        submit_btn.place(x=180, y=355)

    def issue_book(self):
        if self.book_isbn_text.get() == "" or self.library_card_text.get() == "" or self.student_name_text.get() == "" \
                or self.book_title_text.get() == "" or self.issue_date_text.get() == "" or self.return_date_text.get() == "":
            messagebox.showerror("Please include all fields.")
        else:
            conn = sqlite3.connect("library.db")
            cur = conn.cursor()
            # Get record from student table
            cur.execute("SELECT * FROM students WHERE library_card_num LIKE ?", (self.library_card_text.get(),))
            student = cur.fetchone()
            # Get record from books table
            cur.execute("SELECT * FROM books WHERE isbn LIKE ? AND title LIKE ?",
                        (self.book_isbn_text.get(), self.book_title_text.get()))
            book = cur.fetchone()
            # Get record form issue_books table
            cur.execute("SELECT * FROM issue_books WHERE book_isbn LIKE ? AND library_card LIKE ?",
                        (self.book_isbn_text.get(), self.library_card_text.get()))
            is_book = cur.fetchone()
            if student is None:
                messagebox.showerror("Library card or student name doesn't exists!")
            elif book is None:
                messagebox.showerror("Ops! Book not found!")
            elif is_book is None:
                cur.execute("INSERT INTO issue_books VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                            (self.book_isbn_text.get(), self.book_title_text.get(), self.library_card_text.get(),
                             self.student_name_text.get(), self.issue_date_text.get(),
                             self.return_date_text.get()))
                messagebox.showinfo("Book Successfully Issued!")
                conn.commit()
            else:
                messagebox.showerror("Book already issued!")
            conn.close()
            self.fetch_issued()
            self.clear_text()

    def return_page(self):
        self.return_window = Toplevel(self.root)
        self.return_window.title("Library Management")
        self.return_window.geometry("500x400")
        self.return_window.resizable(False, False)
        self.return_window.configure(bg="lightgreen")
        # Create Text Variables
        self.book_isbn_txt = StringVar()
        self.book_title_txt = StringVar()
        self.library_card_txt = StringVar()
        self.student_name_txt = StringVar()
        self.today_date_txt = StringVar()
        # Create title
        title = Label(self.return_window, text="Return Books!", font=("Times 20 italic bold", 30, "underline", "bold"))
        title.place(x=150, y=20)
        # Create buttons
        exit_btn = Button(self.return_window, text="Exit", font="Times 20 italic bold",
                          command=self.return_window.destroy)
        exit_btn.place(x=250, y=355)
        # Create frame
        rtn_frame = LabelFrame(self.return_window, text="Details", font=("Times italic bold", 16), relief=GROOVE)
        rtn_frame.place(x=20, y=70, width=460, height=280)
        # Create labels
        library_card = Label(rtn_frame, text="Library Card No.", font="Times 20 italic bold")
        library_card.grid(row=0, column=0, padx=30, pady=3)
        library_card_entry = Entry(rtn_frame, textvariable=self.library_card_txt, width=16)
        library_card_entry.grid(row=1, column=0, padx=30, pady=3)

        student_name = Label(rtn_frame, text="Student Name", font="Times 20 italic bold")
        student_name.grid(row=0, column=1, padx=30, pady=3)
        student_name_entry = Entry(rtn_frame, textvariable=self.student_name_txt, width=16)
        student_name_entry.grid(row=1, column=1, padx=30, pady=3)

        book_isbn = Label(rtn_frame, text="Book ISBN", font="Times 20 italic bold")
        book_isbn.grid(row=2, column=0, padx=30, pady=3)
        book_isbn_entry = Entry(rtn_frame, textvariable=self.book_isbn_txt, width=16)
        book_isbn_entry.grid(row=3, column=0, padx=30, pady=3)

        book_title = Label(rtn_frame, text="Book Title", font="Times 20 italic bold")
        book_title.grid(row=2, column=1, padx=30, pady=3)
        book_title_entry = Entry(rtn_frame, textvariable=self.book_title_txt, width=16)
        book_title_entry.grid(row=3, column=1, padx=30, pady=3)

        today_date = Label(rtn_frame, text="Today's Date", font="Times 20 italic bold")
        today_date.grid(row=4, column=0, padx=30, pady=3)
        today_date_entry = DateEntry(rtn_frame, textvariable=self.today_date_txt, width=16)
        today_date_entry.grid(row=5, column=0, padx=30, pady=3)
        # Create submit button
        return_btn = Button(self.return_window, text="Return", font="Times 20 italic bold",
                            command=self.return_book)
        return_btn.place(x=180, y=355)

    def return_book(self):
        if self.library_card_txt.get() == "" or self.student_name_txt.get() == "" or self.book_isbn_txt.get() == "" or \
                self.book_title_txt.get() == "" or self.today_date_txt.get() == "":
            messagebox.showerror("Please include all fields")
        else:
            conn = sqlite3.connect("library.db")
            cur = conn.cursor()
            # Get issue_date from issue_books
            cur.execute(
                "SELECT * FROM issue_books WHERE book_isbn LIKE ? AND book_title LIKE ? AND library_card LIKE ?",
                (self.book_isbn_txt.get(), self.book_title_txt.get(), self.library_card_txt.get()))
            record = cur.fetchall()
            if record:
                for date in record:
                    self.iss_book = date[2]
                    self.iss_name = date[4]
                    self.iss_date = date[5]
                    self.rtn_date = date[6]
                    self.returned = self.today_date_txt.get()
                    start = datetime.strptime(self.rtn_date, "%m/%d/%y")
                    end = datetime.strptime(self.returned, "%m/%d/%y")
                    diff = end.date() - start.date()
                    if end.date() > start.date():
                        self.fine = f"Due date exceeded by {diff.days} days.\nYou have ${diff.days * 5} dollar fine!"
                    else:
                        self.fine = f"You are all set {self.iss_name}!"
                    cur.execute("DELETE FROM issue_books WHERE book_isbn LIKE ? AND book_title LIKE ? AND "
                                "library_card LIKE ?", (self.book_isbn_txt.get(), self.book_title_txt.get(),
                                                        self.library_card_txt.get()))
                    messagebox.showinfo("Book Return Successful!")
                    conn.commit()
                    conn.close()
                    self.fetch_issued()
                    # Binding return info with labels
                    self.stu_name_entry.config(text=self.iss_name)
                    self.bk_title_entry.config(text=self.iss_book)
                    self.iss_date_entry.config(text=self.iss_date)
                    self.due_date_entry.config(text=self.rtn_date)
                    self.rtn_date_entry.config(text=self.returned)
                    self.fine_label_entry.configure(text=self.fine)
            else:
                messagebox.showerror("Record not matched!")
            # Clear all fields
            self.library_card_txt.set("")
            self.student_name_txt.set("")
            self.book_isbn_txt.set("")
            self.book_title_txt.set("")

    def clear_text(self):
        self.library_card_text.set("")
        self.student_name_text.set("")
        self.book_isbn_text.set("")
        self.book_title_text.set("")
        self.issue_date_text.set("")
        self.return_date_text.set("")

    def remove_page(self):
        self.remove_window = Toplevel(self.root)
        self.remove_window.title("Library Management")
        self.remove_window.geometry("500x400")
        self.remove_window.resizable(False, False)
        self.remove_window.configure(bg="lightblue")
        # Create text variables
        self.isbn_txt = StringVar()
        self.title_txt = StringVar()
        # Create title
        title = Label(self.remove_window, text="Delete Books!", font=("Times 20 italic bold", 30, "underline", "bold"))
        title.place(x=150, y=20)
        # Create frame
        remove_frame = LabelFrame(self.remove_window, text="Details", font=("Times italic bold", 16), relief=GROOVE)
        remove_frame.place(x=20, y=70, width=460, height=280)
        # Create buttons
        exit_btn = Button(self.remove_window, text="Exit", font="Times 20 italic bold",
                          command=self.remove_window.destroy)
        exit_btn.place(x=250, y=355)
        # Create labels
        isbn = Label(remove_frame, text="BOOK'S ISBN:", font="Times 20 italic bold")
        isbn.grid(row=0, column=0, pady=10)
        isbn_entry = Entry(remove_frame, textvariable=self.isbn_txt, width=18)
        isbn_entry.grid(row=0, column=1, pady=10)
        or_lbl = Label(remove_frame, text="OR", font="Times 20 italic bold")
        or_lbl.grid(row=1, column=0)
        title = Label(remove_frame, text="BOOK'S TITLE:", font="Times 20 italic bold")
        title.grid(row=2, column=0, pady=10)
        title_entry = Entry(remove_frame, textvariable=self.title_txt, width=18)
        title_entry.grid(row=2, column=1, pady=10)
        # Create submit button
        delete_btn = Button(self.remove_window, text="Delete", font="Times 20 italic bold",
                            command=self.remove_book)
        delete_btn.place(x=180, y=355)

    def remove_book(self):
        if self.isbn_txt.get() == "" and self.title_txt.get() == "":
            messagebox.showerror("Record not selected!")
        else:
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM issue_books WHERE book_isbn LIKE ? OR book_title LIKE ?",
                        (self.isbn_txt.get(), self.title_txt.get()))
            bk_rows = cur.fetchone()
            if bk_rows is None:
                messagebox.showerror("Record not found!")
            else:
                cur.execute("DELETE FROM issue_books WHERE book_isbn LIKE ? OR book_title LIKE ?",
                            (self.isbn_txt.get(), self.title_txt.get()))
                messagebox.showinfo("Record Successfully Deleted!")
                conn.commit()
            conn.close()
            self.fetch_issued()
            self.isbn_txt.set("")
            self.title_txt.set("")

    def logout(self):
        self.root.destroy()
        import main