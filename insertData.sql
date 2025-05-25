INSERT INTO book VALUES (1, '1984', 'George Orwell', 'Dystopia', 'Secker & Warburg', 1949);

INSERT INTO staff  VALUES (1, 'Ms. Soha', 'soha@library.com', 'Librarian');

INSERT INTO book (book_ID, title, author, genre, publisher, year_published) VALUES
    (2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 'J.B. Lippincott & Co.', 1960),
    (3, 'Pride and Prejudice', 'Jane Austen', 'Romance', 'T. Egerton', 1813),
    (4, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 'Charles Scribner''s Sons', 1925),
    (5, 'Moby-Dick', 'Herman Melville', 'Adventure', 'Harper & Brothers', 1851),
    (6, 'The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 'Little, Brown and Company', 1951),
    (7, 'Brave New World', 'Aldous Huxley', 'Science Fiction', 'Chatto & Windus', 1932), 
    (8, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 'George Allen & Unwin', 1937),
    (9, ‘Fahrenheit 451', 'Ray Bradbury', 'Dystopia', 'Ballantine Books', 1953),
    (10, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Philosophical Fiction', 'The Russian Messenger', 1866);

INSERT INTO Member (Member_ID, name, email) VALUES
    (20003, 'Fahad Al-Otaibi', 'fahad.alotaibi@example.com'),
    (20004, 'Noura Al-Qahtani', 'noura.qht@example.com'),
    (20005, 'Salman Al-Dosari', 'salman.dosari@example.com'),
    (20006, 'Hind Al-Shahrani', 'hind.shahrani@example.com');

INSERT INTO Staff (Staff_ID, Name, Role) VALUES
    (40003, 'Abdullah Al-Subaie', 'Admin'),
    (40004, 'Reem Al-Zahrani', 'Assistant Librarian'),
    (40005, 'Mohammed Al-Juhani', 'Support'),
    (40006, 'Jawaher Al-Otaibi', 'Manager');

INSERT INTO STAFF (staff_ID, name, position) VALUES
    (40003, 'Abdullah Al-Subaie', 'Admin'),
    (40004, 'Reem Al-Zahrani', 'Assistant Librarian'),
    (40005, 'Mohammed Al-Juhani', 'Support'),
    (40006, 'Jawaher Al-Otaibi', 'Manager');

INSERT INTO Fine (Fine_ID, Member_ID, Amount, Paid_Status) VALUES
    (60003, 20004, 10.00, FALSE),
    (60004, 20005, 0.00, TRUE),
    (60005, 20006, 2.50, FALSE);
