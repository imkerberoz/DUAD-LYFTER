-- =============================================
-- 1. CREACION DE TABLAS
-- =============================================

CREATE TABLE IF NOT EXISTS Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Author INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);

CREATE TABLE IF NOT EXISTS Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT
);

CREATE TABLE IF NOT EXISTS Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER,
    CustomerID INTEGER,
    State TEXT,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);

-- =============================================
-- 2. INSERTAR DATOS
-- =============================================

INSERT OR IGNORE INTO Authors VALUES 
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT OR IGNORE INTO Books VALUES 
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball', 4),
(5, 'The Book of the 5 Rings', NULL);

INSERT OR IGNORE INTO Customers VALUES 
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

INSERT OR IGNORE INTO Rents VALUES 
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


-- ===========================================================================
-- CONSULTAS: 
-- ==========================================================================

-- PRIMERA: Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT 
    b.ID AS Book_ID,
    b.Name AS Book_Name,
    a.Name AS Author_Name
FROM Books b
LEFT JOIN Authors a ON b.Author = a.ID;

--SEGUNDA: Obtenga todos los libros que no tienen autor
SELECT 
    ID, Name 
FROM Books 
WHERE Author IS NULL;

-- TERCERA: Obtenga todos los autores que no tienen libros
SELECT 
    a.ID, a.Name
FROM Authors a
LEFT JOIN Books b ON a.ID = b.Author
WHERE b.ID IS NULL;

--CUARTA: Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT
    b.ID, b.Name
FROM Books b
INNER JOIN Rents r ON b.ID = r.BookID;

-- QUINtA: Obtenga todos los libros que nunca han sido rentados
SELECT 
    b.ID, b.Name
FROM Books b
LEFT JOIN Rents r ON b.ID = r.BookID
WHERE r.ID IS NULL;

--SEXTA: Obtenga todos los clientes que nunca han rentado un libro
SELECT 
    c.ID, c.Name
FROM Customers c
LEFT JOIN Rents r ON c.ID = r.CustomerID
WHERE r.ID IS NULL;

-- SEPTIMA: Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT DISTINCT
    b.ID, b.Name, r.State
FROM Books b
INNER JOIN Rents r ON b.ID = r.BookID
WHERE r.State = 'Overdue';



