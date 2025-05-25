# library-management-system
a command-line Python program that lets users manage library books, members, and lending information by connecting to a MySQL database.  This project was made to show showcase database and backend integration as part of my computer science education.

##  Features

- Add, update, and search for books
- Add, update, and search for members
- Record book loans and returns
- Track overdue books and apply fines
- View loan history by member
- SQL queries for reporting and analysis

## Technologies Used

- **Python 3**
- **MySQL**
- **MySQL Connector (mysql-connector-python)**
- **MySQL Workbench** (for database design)

## Files Included

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `library_app.py`   | Main Python script to run the app            |
| `createTables.sql` | SQL script to create all tables              |
| `insertData.sql`   | SQL script to populate sample data           |
| `Queries.sql`      | Helpful example queries and reports          |

## How to Run

1. Install MySQL and Python 3
2. Run `createTables.sql` in MySQL to create the schema
3. Run `insertData.sql` to load test data
4. Make sure `mysql-connector-python` is installed:
   ```bash
   pip install mysql-connector-python

## Author 
Galiah Badokhon 
Computer Science student
