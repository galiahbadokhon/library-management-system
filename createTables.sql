CREATE DATABASE libraryDB;
CREATE TABLE book (
    book_ID INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(100),
    publisher VARCHAR(255),
    year_published YEAR );

CREATE TABLE member (
    member_ID INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    membership_date DATE);

 CREATE TABLE staff (
    staff_ID INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    position VARCHAR(100)
    );

CREATE TABLE loan (
    loan_ID INT PRIMARY KEY,
    member_ID INT,
    book_ID INT,
    staff_ID INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_ID) REFERENCES member(member_ID),
    FOREIGN KEY (book_ID) REFERENCES book(book_ID));

CREATE TABLE studentMember (
    member_ID INT PRIMARY KEY,
    school_name VARCHAR(255),
    FOREIGN KEY (member_ID) REFERENCES member(member_ID)
    );

CREATE TABLE facultyMember (
    member_ID INT PRIMARY KEY,
    department VARCHAR(255),
    FOREIGN KEY (member_ID) REFERENCES member(member_ID)
    );


CREATE TABLE reservation ( reservation_ID INT PRIMARY KEY, book_ID INT, member_ID INT, reservation_date DATE, FOREIGN KEY (book_ID) REFERENCES book(book_ID), FOREIGN KEY (member_ID) REFERENCES member(member_ID));

CREATE TABLE fine ( fine_ID INT PRIMARY KEY, member_ID INT, amount DECIMAL (6,2), paid_status BOOLEAN, FOREIGN KEY (member_ID) REFERENCES member(member_ID));

