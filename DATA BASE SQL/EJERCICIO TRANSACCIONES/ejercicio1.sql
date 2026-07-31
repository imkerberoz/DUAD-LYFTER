-- =============================================
-- EJERCICIO 1: Creación de la Base de Datos
-- =============================================

-- 1. Tabla de Usuarios
CREATE TABLE IF NOT EXISTS users (                     -- Crea la tabla solo si no existe
    user_id SERIAL PRIMARY KEY,                        -- ID automático (clave primaria)
    username VARCHAR(50) UNIQUE NOT NULL,              -- Nombre de usuario único y obligatorio
    email VARCHAR(100) UNIQUE NOT NULL,                -- Correo único y obligatorio
    full_name VARCHAR(100) NOT NULL,                   -- Nombre completo obligatorio
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Fecha de creación automática
);

-- 2. Tabla de Productos
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,                     -- ID automático del producto
    name VARCHAR(100) NOT NULL,                        -- Nombre del producto
    description TEXT,                                  -- Descripción (puede ser larga)
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0),   -- Precio con 2 decimales (debe ser > 0)
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0), -- Cantidad en inventario (no puede ser negativa)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Fecha de creación
);

-- 3. Tabla de Facturas
CREATE TABLE IF NOT EXISTS bills (
    bill_id SERIAL PRIMARY KEY,                        -- ID automático de la factura
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE, -- Relación con el usuario (si se borra el usuario, se borran sus facturas)
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Fecha de la factura
    total_amount NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK (total_amount >= 0), -- Total de la factura
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'cancelled', 'returned')) -- Estado permitido
);

-- 4. Tabla cruz (ítems de cada factura)
CREATE TABLE IF NOT EXISTS bill_items (
    bill_item_id SERIAL PRIMARY KEY,                   -- ID automático del ítem
    bill_id INTEGER REFERENCES bills(bill_id) ON DELETE CASCADE, -- Relación con la factura
    product_id INTEGER REFERENCES products(product_id) ON DELETE RESTRICT, -- Relación con el producto (no permite borrar producto si está en una factura)
    quantity INTEGER NOT NULL CHECK (quantity > 0),    -- Cantidad comprada (debe ser mayor a 0)
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price > 0), -- Precio unitario al momento de la compra
    subtotal NUMERIC(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED -- Se calcula automáticamente
);

-- Índices (mejoran la velocidad de las búsquedas)
CREATE INDEX IF NOT EXISTS idx_bills_user_id ON bills(user_id);           -- Índice para buscar facturas por usuario
CREATE INDEX IF NOT EXISTS idx_bill_items_bill_id ON bill_items(bill_id); -- Índice para buscar ítems por factura
CREATE INDEX IF NOT EXISTS idx_bill_items_product_id ON bill_items(product_id); -- Índice para buscar ítems por producto

-- Datos de ejemplo: Usuarios
INSERT INTO users (username, email, full_name) 
VALUES 
    ('juanperez', 'juan@example.com', 'Juan Pérez'),
    ('mariagomez', 'maria@example.com', 'María Gómez')
ON CONFLICT (username) DO NOTHING;                     -- Si el usuario ya existe, no lo vuelve a insertar

-- Datos de ejemplo: Productos (forma segura para evitar duplicados)
INSERT INTO products (name, description, price, stock)
SELECT 'Laptop Dell', 'Laptop de 15 pulgadas', 899.99, 50
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Laptop Dell')
UNION ALL
SELECT 'Mouse Inalámbrico', 'Mouse ergonómico', 29.99, 200
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Mouse Inalámbrico')
UNION ALL
SELECT 'Teclado Mecánico', 'Teclado RGB', 79.99, 100
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Teclado Mecánico');