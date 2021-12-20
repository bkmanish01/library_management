import sqlite3




class Database:
    def __init__(self, db):
        self.conn = None
        try:
            # Connect Database
            self.conn = sqlite3.connect(db)
            self.cur = self.conn.cursor()
            # Create Tables
            self.cur.execute("CREATE TABLE IF NOT EXISTS librarians ("
                             "librarian_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                             "first_name TEXT NOT NULL, "
                             "last_name TEXT NOT NULL, "
                             "phone INT NOT NULL, "
                             "email TEXT NOT NULL,"
                             "username TEXT NOT NULL, "
                             "password TEXT NOT NULL,"
                             "UNIQUE (first_name, last_name, phone, email, username, password) ON CONFLICT IGNORE)")

            self.cur.execute("CREATE TABLE IF NOT EXISTS students ("
                             "student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                             "library_card_num TEXT NOT NULL, "
                             "first_name TEXT NOT NULL, "
                             "last_name TEXT NOT NULL, "
                             "address TEXT NOT NULL, "
                             "city TEXT NOT NULL, "
                             "state TEXT NOT NULL, "
                             "zip INTEGER NOT NULL, "
                             "phone INT NOT NULL, "
                             "email TEXT NOT NULL, "
                             "username TEXT NOT NULL, "
                             "password TEXT NOT NULL,"
                             "UNIQUE (library_card_num, first_name, last_name, phone, email, username , password)"
                             "ON CONFLICT IGNORE)")

            self.cur.execute("CREATE TABLE IF NOT EXISTS books ("
                             "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                             "isbn TEXT NOT NULL, "
                             "title TEXT NOT NULL, "
                             "genre TEXT NOT NULL, "
                             "author_first TEXT NOT NULL,"
                             "author_last TEXT NOT NULL,"
                             "publisher TEXT NOT NULL, "
                             "categories TEXT NOT NULL,"
                             "description TEXT NOT NULL,"
                             "UNIQUE (isbn, title) ON CONFLICT IGNORE)")

            self.cur.execute("CREATE TABLE IF NOT EXISTS issue_books ("
                             "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                             "book_isbn TEXT NOT NULL,"
                             "book_title TEXT NOT NULL, "
                             "library_card TEXT NOT NULL, "
                             "student_name TEXT NOT NULL, "
                             "issued_date TEXT NOT NULL,"
                             "return_date TEXT NOT NULL,"
                             "UNIQUE (book_isbn, book_title, library_card, student_name) ON CONFLICT IGNORE)")
            # Insert records into librarian table
            self.cur.execute("INSERT INTO librarians (first_name, last_name, phone, email, username, "
                             "password) VALUES ('Robert', 'Keystone', '9999999999', 'keyrobert@jpg.com', 'Keystone1', "
                             "'Mountain123')")
            self.cur.execute("INSERT INTO librarians (first_name, last_name, phone, email, username, "
                             "password) VALUES ('Hillary', 'Farmer', '8888888888', 'farhillary@jpg.edu', 'Farmer01', "
                             "'Boulder123')")
            # Insert records into student table
            self.cur.execute("INSERT INTO students (library_card_num, first_name, last_name, address, "
                             "city, state, zip,  phone, email,  username,  password) VALUES ('S909090', 'Harry', "
                             "'Thapa', '100 Everest St', 'Boulder', 'CO', '11111', '7777777777', "
                             " 'thapaharry@ghi.org', 'Thapa12', 'Everest90')")
            self.cur.execute("INSERT INTO students (library_card_num, first_name, last_name, address, city, "
                             "state,  zip,  phone, email,  username,  password) VALUES ('S808080', 'Julie', 'Karki', "
                             "'150 Pine St', 'Boulder', 'CO', '11111', '6666666666', 'karkijulie@ghi.com', "
                             "'Karki100', 'Lukla01')")
            self.cur.execute("INSERT INTO students (library_card_num, first_name, last_name, address, city, "
                             "state, zip,  phone, email,  username,  password) VALUES ('S707070', 'Jack', 'Fung', "
                             "'200 Ski Ave', 'Boulder', 'CO', '11111', '5555555555', 'fungjack@ghi.edu', 'Fung100', "
                             "'Lake001')")
            # Insert records into books table
            self.cur.execute("INSERT INTO books(isbn, title, genre, author_first, author_last, publisher, "
                             "categories, description) VALUES('1-305-25103-2', 'SQL', 'Tech.', 'Joan', "
                             "'Casteel', 'jpf.inc', 'General', 'This is database book')")
            self.cur.execute("INSERT INTO books(isbn, title, genre, author_first, author_last, publisher, "
                             "categories, description) VALUES('1-234-56789-0', 'Mt.Everest', 'Novel', 'Manish', "
                             "'Bishow', 'hld.inc', 'Individual', 'This is great novel')")
            self.cur.execute("INSERT INTO books(isbn, title, genre, author_first, author_last, publisher, "
                             "categories, description) VALUES('4-234-23453-1', 'Annapurna', 'Story', 'Robert', "
                             "'Keyston', 'com.inc', 'Individual','This is real story')")
            self.cur.execute("INSERT INTO books(isbn, title, genre, author_first, author_last, publisher, "
                             "categories, description) VALUES('0538745843', 'PHP', 'Tech.', 'Don', "
                             "'Gosselin', 'Cengage', 'General','Great for backend dev.')")
            self.conn.commit()
            self.cur.close()
        except Exception as e:
            print('Error thrown during create_db()')
            print(e)
        finally:
            if self.conn:
                self.conn.close()


db = Database('library.db')
