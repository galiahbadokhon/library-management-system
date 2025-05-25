import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ghaliaA2005",
        database="libraryDB"
    )

def show_menu():
    print("\n--- Library Menu ---")
    print("1. Show all books")
    print("2. Update books")
    print("3. Add a member")
    print("4. Update member information")
    print("5. Record a loan")
    print("6. Return a book")
    print("7. View fines")
    print("8. View loan history")
    print("9. Exit")

def get_memberID(cursor, name):
     cursor.execute("SELECT member_ID, name FROM member WHERE name LIKE %s", ('%' + name + '%',))
     return cursor.fetchall()

def get_staffID(cursor, name):
    cursor.execute("SELECT staff_ID, name FROM staff WHERE name LIKE %s", ('%' + name + '%',))
    return cursor.fetchall()

def get_bookID(cursor, title):
    cursor.execute("SELECT book_ID FROM book WHERE title = %s", (title,))
    result = cursor.fetchone()
    return result[0] if result else None

def view_loan(cursor):
    name = input("Enter member name to view loan history: ")
    cursor.execute("""
        SELECT m.name, b.title, l.loan_date, l.return_date
        FROM loan l
        JOIN member m ON l.member_ID = m.member_ID
        JOIN book b ON l.book_ID = b.book_ID
        WHERE m.name LIKE %s
        ORDER BY l.loan_date DESC
     """, ('%' + name + '%',))
    results = cursor.fetchall()

    if results:
        print("/n--- Loab History ---")
        for row in results:
            return_info=row[3] if row[3] else "Not returned yet"
            print(f"Member: {row[0]} | Book: {row[1]} | Loaned: {row[2]} | Returned: {return_info}")
        else:
            print("No loan history found for that name")
    

def main():
    conn = connect_db()
    cursor = conn.cursor()

    # Show active loans at the start
    cursor.execute("""
        SELECT loan_ID, member_ID, book_ID, loan_date 
        FROM loan 
        WHERE return_date IS NULL
    """)
    loans = cursor.fetchall()
    print("\n--- Active Loans ---")
    for loan in loans:
        print(f"Loan ID: {loan[0]}, Member ID: {loan[1]}, Book ID: {loan[2]}, Loan Date: {loan[3]}")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            cursor.execute("SELECT book_ID, title, author FROM book")
            books = cursor.fetchall()
            print("\n--- Book List ---")
            for book in books:
                print(f"{book[0]} - {book[1]} by {book[2]}")

        elif choice == "2":
            title = input("Enter book title to search: ")
            cursor.execute("SELECT book_ID, title, author, publisher, year_published FROM book WHERE title LIKE %s", ('%' + title + '%',))
            results = cursor.fetchall()

            if not results:
                print("No books found.")
                return
            
            print("\nMatching books:")
            for book in results:
                print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Publisher: {book[3]} | Year; {book[4]}")

            book_id = input("Enter the ID of the book you want to update: ")

            print("What do you want to update")
            print("1. Title")
            print("2. Author")
            print("3. Publisher")
            print("4. Year")
            choice = input("Choose an option (1-4)")

            fields = {"1": "title", "2": "author", "3": "publisher", "4": "year_published"}
            field = fields.get(choice)

            if not field:
                print("Invaild choice")
                
                return

            new_value = input(f"Enter new {field}")

            if field == "year" and not new_value.isdigit():
                print("Year must be a number.")
                return

            cursor.execute(f"UPDATE book SET {field} = %s WHERE book_ID = %s", (new_value, book_id))
            conn.commit()
            print("Book information updated.")

        elif choice == "3":
            name = input("Member name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            cursor.execute(
                "INSERT INTO member (name, email, phone, membership_date) VALUES (%s, %s, %s, CURDATE())",
                (name, email, phone)
            )
            conn.commit()
            new_member_id = cursor.lastrowid
            print(f"Member added! Your member ID is: {new_member_id}")

        elif choice == "4":
            print("If you forgot the member ID type 'lookup'.")
            member_id = input("Enter member ID or type 'lookup': ").strip()

            if member_id.lower() == 'lookup':
                name = input("Enter member name to search: ")
                results = get_memberID(cursor, name)
                if results:
                    print("Matching members:")
                    for mid, mname in results:
                        print(f"ID: {mid}, Name: {mname}")
                    member_id = input("Now enter the correct member ID from above: ")
                else:
                    print("No member found.")

            print("What do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            update_choice = input("Enter an option (1-3): ")

            if update_choice == "1":
                new_name = input("Enter new name: ")
                cursor.execute("UPDATE member SET name = %s WHERE member_ID = %s", (new_name, member_id))
                
            elif update_choice == "2":
                new_email = input("Enter new email: ")
                cursor.execute("UPDATE member SET email = %s WHERE member_ID = %s", (new_email, member_id))

            elif choice == "3":
                new_phone = input("Enter new phone number: ")
                cursor.execute("UPDATE member SET phone = %s WHERE member_ID %s", (new_phone, member_id))

            else:
                print("Invaild choice.")
                return

            conn.commit()
            print("New member information updated.")
             
            

        elif choice == "5":
            print("If you forgot your member ID, type 'lookup', otherwise enter Member ID:")
            member_id = input("Member ID or 'lookup': ").strip()
            if member_id.lower() == "lookup":
                name = input("Enter member name to search: ")
                results = get_memberID(cursor, name)
                if results:
                    print("Matching members:")
                    for mid, mname in results:
                        print(f"ID: {mid}, Name: {mname}")
                    member_id = input("Now enter the correct member ID from above: ")
                else:
                    print("No members found with that name.")
                    continue

            title = input("Book title: ")
            book_id = get_bookID(cursor, title)
            if not book_id:
                print("Book not found.")
                continue

            print("If you forgot the staff ID, type 'lookup', otherwise enter staff ID:")
            staff_id = input("Staff ID or 'lookup': ").strip()
            if staff_id.lower() == "lookup":
                name = input("Enter staff name to search: ")
                results = get_staffID(cursor, name)
                if results:
                    print("Matching staff:")
                    for sid, sname in results:
                        print(f"ID: {sid}, Name: {sname}")
                    staff_id = input("Now enter the correct staff ID from above: ")
                else:
                    print("No staff found with that name.")
                    continue

            cursor.execute(
                "INSERT INTO loan (member_ID, book_ID, staff_ID, loan_date) VALUES (%s, %s, %s, CURDATE())",
                (member_id, book_id, staff_id)
            )
            conn.commit()
            print("Loan recorded.")

        elif choice == "6":
            loan_id = input("Enter loan ID of the book being returned: ")
            cursor.execute("SELECT loan_date FROM loan WHERE loan_ID = %s AND return_date IS NULL", (loan_id,))
            result = cursor.fetchone()

            if result:
                loan_date = result[0]
                return_date = datetime.today().date()
                cursor.execute("UPDATE loan SET return_date = %s WHERE loan_ID = %s", (return_date, loan_id))

                days_loaned = (return_date - loan_date).days
                if days_loaned > 14:
                    fine_amount = (days_loaned - 14) * 1.0
                    cursor.execute("INSERT INTO fine (loan_ID, amount) VALUES (%s, %s)", (loan_id, fine_amount))
                    print(f"Book returned late. Fine of ${fine_amount}")
                else:
                    print("Book returned on time.")
                conn.commit()
            else:
                print("Invalid loan ID or book already returned.")

        elif choice == "7":
            cursor.execute("""
                SELECT m.name, SUM(f.amount) AS total_fines
                FROM fine f
                JOIN loan l ON f.loan_ID = l.loan_ID
                JOIN member m ON l.member_ID = m.member_ID
                GROUP BY m.member_ID
            """)
            results = cursor.fetchall()
            print("\n--- Fines ---")
            for row in results:
                print(f"{row[0]} - ${row[1]}")

        elif choice == "8":
            view_loan(cursor)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
