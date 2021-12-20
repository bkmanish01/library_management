import sqlite3
from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox




# Create window object
class LibrarianWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("950x600")
        self.root.resizable(False, False)
        # Create frame
        detail_frame = LabelFrame(self.root, text="Records", font=("Times italic bold", 20), bd=5, relief=GROOVE)
        detail_frame.place(x=20, y=90, width=400, height=480)

        command_frame = LabelFrame(self.root, text="Commands", font=("Times italic bold", 16),
                                   bg="lightgray", relief=GROOVE)
        command_frame.place(x=20, y=465, width=395, height=100)

        data_frame = Frame(self.root)
        data_frame.place(x=430, y=90, width=500, height=480)

        search_frame = Frame(data_frame, bg="lightgray", bd=5, relief=FLAT)
        search_frame.pack(side=TOP, fill=X)

        display_frame = Frame(data_frame, bd=5, relief=GROOVE)
        display_frame.pack(fill=BOTH, expand=True)
        # Create Text Variables
        self.isbn = StringVar()
        self.title = StringVar()
        self.genre = StringVar()
        self.auth_first = StringVar()
        self.auth_last = StringVar()
        self.publisher = StringVar()
        self.categories = StringVar()
        self.description = StringVar()
        self.search = StringVar()
        # Create label and entry
        isbn_label = Label(detail_frame, text="ISBN:", font=("Arial bold", 15), pady=10)
        isbn_label.grid(row=0, column=0, sticky=E)
        isbn_entry = Entry(detail_frame, textvariable=self.isbn)
        isbn_entry.grid(row=0, column=1)

        title_label = Label(detail_frame, text="TITLE:", font=("Arial bold", 15), pady=10)
        title_label.grid(row=1, column=0, sticky=E)
        title_entry = Entry(detail_frame, textvariable=self.title)
        title_entry.grid(row=1, column=1)

        genre_label = Label(detail_frame, text="GENRE:", font=("Arial bold", 15), pady=10)
        genre_label.grid(row=2, column=0, sticky=E)
        genre_entry = Entry(detail_frame, textvariable=self.genre)
        genre_entry.grid(row=2, column=1)

        auth_first_label = Label(detail_frame, text="AUTHOR FIRST NAME:", font=("Arial bold", 15), pady=10)
        auth_first_label.grid(row=3, column=0, sticky=E)
        auth_first_entry = Entry(detail_frame, textvariable=self.auth_first)
        auth_first_entry.grid(row=3, column=1)

        auth_last_label = Label(detail_frame, text="AUTHOR LAST NAME:", font=("Arial bold", 15), pady=10)
        auth_last_label.grid(row=4, column=0, sticky=E)
        auth_last_entry = Entry(detail_frame, textvariable=self.auth_last)
        auth_last_entry.grid(row=4, column=1)

        publisher_label = Label(detail_frame, text="PUBLISHER:", font=("Arial bold", 15), pady=10)
        publisher_label.grid(row=5, column=0, sticky=E)
        publisher_entry = Entry(detail_frame, textvariable=self.publisher)
        publisher_entry.grid(row=5, column=1)

        categories_label = Label(detail_frame, text="CATEGORIES:", font=("Arial bold", 15), pady=10)
        categories_label.grid(row=6, column=0, sticky=E)
        categories_entry = Entry(detail_frame, textvariable=self.categories)
        categories_entry.grid(row=6, column=1)

        description_label = Label(detail_frame, text="DESCRIPTION:", font=("Arial bold", 15), pady=10)
        description_label.grid(row=7, column=0, sticky=E)
        description_entry = Entry(detail_frame, textvariable=self.description)
        description_entry.grid(row=7, column=1)

        # Create logout button
        logout_btn = Button(self.root, text='Logout', font=("Arial bold", 15), fg='red', width=8, command=self.logout)
        logout_btn.place(x=850, y=50)
        # Create buttons
        add_btn = Button(command_frame, text='Add', font=("Arial bold", 15), width=8, command=self.add_item, padx=3)
        add_btn.grid(row=0, column=0, padx=10, pady=20)

        remove_btn = Button(command_frame, text='Remove', font=("Arial bold", 15), width=8, command=self.remove_item)
        remove_btn.grid(row=0, column=1, padx=10)

        update_btn = Button(command_frame, text='Update', font=("Arial bold", 15), width=8, command=self.update_item)
        update_btn.grid(row=0, column=2, padx=10)

        clear_btn = Button(command_frame, text='Clear', font=("Arial bold", 15), width=8, command=self.clear_text)
        clear_btn.grid(row=0, column=3, padx=10)
        # Create search button
        search_btn = Button(search_frame, text="Search", font=("Arial bold", 16), bg="lightgray", width=10,
                            command=self.search_item)
        search_btn.grid(row=0, column=2, pady=2)
        search_entry = Entry(search_frame, width=12, textvariable=self.search)
        search_entry.grid(row=0, column=1, padx=5, pady=2)
        self.search_by = ttk.Combobox(search_frame, value=["ISBN", "Title", "Publisher"], font=("Arial", 14), width=12)
        self.search_by.current(0)
        self.search_by.grid(row=0, column=0, pady=2)
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
        self.book_table.pack(fill=BOTH, expand=True)

        self.populate_list()
        self.book_table.bind("<ButtonRelease-1>", self.fetch_data)

    def populate_list(self):
        conn = sqlite3.connect("library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for row in rows:
                self.book_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def add_item(self):
        if self.isbn.get() == "" or self.title.get() == "" or self.genre.get() == "" or self.auth_first.get() == "" or \
                self.auth_last.get() == "" or self.publisher.get() == "" or self.categories.get() == "" or \
                self.description.get() == "":
            messagebox.showerror("Please include all fields")
        else:
            conn = sqlite3.connect("library.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE isbn LIKE ? or title LIKE ?",
                        (self.isbn.get(), self.title.get()))
            result_row = cur.fetchall()
            if result_row:
                messagebox.showerror("Book Already Exists!")
            else:
                cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (self.isbn.get(), self.title.get(), self.genre.get(), self.auth_first.get(),
                             self.auth_last.get(), self.publisher.get(), self.categories.get(), self.description.get()))
                messagebox.showinfo("Record Successfully Added!")
                conn.commit()
            conn.close()
            self.populate_list()
            self.clear_text()

    def fetch_data(self, event):
        cur_row = self.book_table.focus()
        content = self.book_table.item(cur_row)
        row = content["values"]
        self.isbn.set(row[1])
        self.title.set(row[2])
        self.genre.set(row[3])
        self.auth_first.set(row[4])
        self.auth_last.set(row[5])
        self.publisher.set(row[6])
        self.categories.set(row[7])
        self.description.set(row[8])

    def remove_item(self):
        if self.isbn.get() == "" or self.title.get() == "" or self.genre.get() == "" or self.auth_first.get() == "" or \
                self.auth_last.get() == "" or self.publisher.get() == "" or self.categories.get() == "" or \
                self.description.get() == "":
            messagebox.showerror("Record not selected!")
        else:
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE isbn=? OR title=? OR publisher=?",
                        (self.isbn.get(), self.title.get(), self.publisher.get()))
            messagebox.showinfo("Record Successfully Deleted!")
            conn.commit()
            conn.close()
            self.populate_list()
            self.clear_text()

    def update_item(self):
        if self.isbn.get() == "" or self.title.get() == "" or self.genre.get() == "" or self.auth_first.get() == "" or \
                self.auth_last.get() == "" or self.publisher.get() == "" or self.categories.get() == "" or \
                self.description.get() == "":
            messagebox.showerror("Record not selected!")
        else:
            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute("UPDATE books SET isbn=?, title=?, genre=?, author_first=?, author_last=?, publisher=?, "
                        "categories=?, description=? WHERE isbn=? OR title=? OR publisher=?",
                        (self.isbn.get(), self.title.get(), self.genre.get(), self.auth_first.get(),
                         self.auth_last.get(), self.publisher.get(), self.categories.get(), self.description.get(),
                         self.isbn.get(), self.title.get(), self.publisher.get()))
            messagebox.showinfo("Record Successfully Updated!")
            conn.commit()
            conn.close()
            self.populate_list()
            self.clear_text()

    def clear_text(self):
        self.isbn.set("")
        self.title.set("")
        self.genre.set("")
        self.auth_first.set("")
        self.auth_last.set("")
        self.publisher.set("")
        self.categories.set("")
        self.description.set("")

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

    def logout(self):
        self.root.destroy()
        import main
