-- =============================================
-- EJERCICIO SQL - lyfters
-- Base de Datos Tienda
-- =============================================

-- 1. CREACIÓN DE TABLAS

CREATE TABLE Products (
    code            TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    price           REAL NOT NULL,
    entry_date      DATE NOT NULL,
    brand           TEXT,
    stock_available INTEGER DEFAULT 0
);

CREATE TABLE Invoices (
    invoice_number  TEXT PRIMARY KEY,
    purchase_date   DATETIME NOT NULL,
    buyer_email     TEXT NOT NULL,
    total_amount    REAL NOT NULL
);

CREATE TABLE Invoice_Items (
    invoice_number  TEXT NOT NULL,
    product_code    TEXT NOT NULL,
    quantity        INTEGER NOT NULL,
    unit_price      REAL NOT NULL,
    line_amount     REAL NOT NULL,
    
    PRIMARY KEY (invoice_number, product_code),
    FOREIGN KEY (invoice_number) REFERENCES Invoices(invoice_number),
    FOREIGN KEY (product_code)   REFERENCES Products(code)
);

CREATE TABLE Shopping_Cart (
    cart_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email     TEXT NOT NULL,
    product_code    TEXT NOT NULL,
    quantity        INTEGER NOT NULL DEFAULT 1,
    added_date      DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (product_code) REFERENCES Products(code)
);

-- 2. MODIFICACIÓN DE TABLA (ALTER TABLE)

ALTER TABLE Invoices ADD COLUMN buyer_phone TEXT;
ALTER TABLE Invoices ADD COLUMN cashier_code TEXT;

-- 3. INSERTAR DATOS DE PRUEBA

INSERT INTO Products (code, name, price, entry_date, brand, stock_available)
VALUES 
('P001', 'Laptop Dell', 1250000, '2025-01-15', 'Dell', 8),
('P002', 'Mouse Inalámbrico', 45000, '2025-02-01', 'Logitech', 25),
('P003', 'Teclado Mecánico', 85000, '2025-03-10', 'Corsair', 12),
('P004', 'Monitor 27"', 320000, '2025-04-05', 'Samsung', 5);

INSERT INTO Invoices (invoice_number, purchase_date, buyer_email, buyer_phone, cashier_code, total_amount)
VALUES 
('F00001', '2026-05-20 10:30:00', 'juan.perez@gmail.com', '8765-4321', 'CAJ01', 1295000),
('F00002', '2026-05-21 14:15:00', 'maria.lopez@hotmail.com', '8877-1122', 'CAJ02', 45000),
('F00003', '2026-05-22 09:45:00', 'juan.perez@gmail.com', '8765-4321', 'CAJ01', 85000);

INSERT INTO Invoice_Items (invoice_number, product_code, quantity, unit_price, line_amount)
VALUES 
('F00001', 'P001', 1, 1250000, 1250000),
('F00002', 'P002', 1, 45000, 45000),
('F00003', 'P003', 1, 85000, 85000);

-- 4. CONSULTAs (SELECT)

-- a) Todos los productos
SELECT * FROM Products;

-- b) Productos con precio mayor a 50000
SELECT * FROM Products WHERE price > 50000;

-- c) Todas las compras de un mismo producto por código
SELECT ii.*, i.purchase_date, i.buyer_email 
FROM Invoice_Items ii 
JOIN Invoices i ON ii.invoice_number = i.invoice_number 
WHERE ii.product_code = 'P001';

-- d) Compras agrupadas por producto
SELECT 
    p.name AS producto,
    SUM(ii.quantity) AS total_unidades_vendidas,
    SUM(ii.line_amount) AS total_dinero_generado
FROM Invoice_Items ii 
JOIN Products p ON ii.product_code = p.code 
GROUP BY p.code, p.name;

-- e) Todas las facturas de un mismo comprador
SELECT * FROM Invoices WHERE buyer_email = 'juan.perez@gmail.com';

-- f) Facturas ordenadas por monto total descendente
SELECT * FROM Invoices ORDER BY total_amount DESC;

-- g) Una sola factura por número
SELECT * FROM Invoices WHERE invoice_number = 'F00001';