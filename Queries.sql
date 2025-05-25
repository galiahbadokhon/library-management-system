SELECT * FROM book WHERE genre = 'Dystopia';

SELECT * FROM member WHERE membership_date > '2023-01-01';

SELECT name, position FROM staff;

SELECT r.reservation_ID, m.name AS member_name, r.reservation_date
FROM reservation r
JOIN member m ON r.member_ID = m.member_ID
WHERE r.book_ID = 1;

SELECT l.loan_ID, m.name AS member_name, b.title, l.loan_date, l.return_date
FROM loan l
JOIN member m ON l.member_ID = m.member_ID
JOIN book b ON l.book_ID = b.book_ID
WHERE l.staff_ID = 1;

SELECT m.name, SUM(f.amount) AS total_fines
FROM fine f
JOIN member m ON f.member_ID = m.member_ID
GROUP BY m.member_ID;

SELECT m.name, s.school_name
FROM studentMember s
JOIN member m ON s.member_ID = m.member_ID;

SELECT m.name, f.department
FROM facultyMember f
JOIN member m ON f.member_ID = m.member_ID;
