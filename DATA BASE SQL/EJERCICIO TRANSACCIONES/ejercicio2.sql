-- =============================================
-- EJERCICIO 2: Transacción de Compra
-- =============================================

DO $$
DECLARE
    -- Variables que usaremos en la transacción
    v_user_id INTEGER := 1;                    -- ID del usuario que compra (Juan Pérez)
    v_bill_id INTEGER;                         -- Aquí guardaremos el ID de la factura creada
    v_product1_id INTEGER := 1;                -- Laptop Dell
    v_product2_id INTEGER := 2;                -- Mouse Inalámbrico
    v_qty1 INTEGER := 2;                       -- Cantidad de laptops a comprar
    v_qty2 INTEGER := 3;                       -- Cantidad de mouse a comprar
    v_stock1 INTEGER;                          -- Stock actual del producto 1
    v_stock2 INTEGER;                          -- Stock actual del producto 2
    v_price1 NUMERIC(10,2);                    -- Precio del producto 1
    v_price2 NUMERIC(10,2);                    -- Precio del producto 2
    v_total NUMERIC(10,2);                     -- Total de la factura
BEGIN
    -- ========================================
    -- 1. Validar que el usuario existe
    -- ========================================
    IF NOT EXISTS (SELECT 1 FROM users WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe', v_user_id;
    END IF;

    -- ========================================
    -- 2. Validar stock suficiente del producto 1
    -- ========================================
    SELECT stock, price INTO v_stock1, v_price1
    FROM products
    WHERE product_id = v_product1_id;

    IF v_stock1 IS NULL THEN
        RAISE EXCEPTION 'El producto con ID % no existe', v_product1_id;
    END IF;

    IF v_stock1 < v_qty1 THEN
        RAISE EXCEPTION 'Stock insuficiente del producto %. Disponible: %, Solicitado: %', 
            v_product1_id, v_stock1, v_qty1;
    END IF;

    -- ========================================
    -- 3. Validar stock suficiente del producto 2
    -- ========================================
    SELECT stock, price INTO v_stock2, v_price2
    FROM products
    WHERE product_id = v_product2_id;

    IF v_stock2 IS NULL THEN
        RAISE EXCEPTION 'El producto con ID % no existe', v_product2_id;
    END IF;

    IF v_stock2 < v_qty2 THEN
        RAISE EXCEPTION 'Stock insuficiente del producto %. Disponible: %, Solicitado: %', 
            v_product2_id, v_stock2, v_qty2;
    END IF;

    -- ========================================
    -- 4. Calcular el total de la factura
    -- ========================================
    v_total := (v_price1 * v_qty1) + (v_price2 * v_qty2);

    -- ========================================
    -- 5. Insertar la factura
    -- ========================================
    INSERT INTO bills (user_id, total_amount, status)
    VALUES (v_user_id, v_total, 'completed')
    RETURNING bill_id INTO v_bill_id;          -- Guardamos el ID de la factura creada

    -- ========================================
    -- 6. Insertar los ítems de la factura
    -- ========================================
    INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
    VALUES 
        (v_bill_id, v_product1_id, v_qty1, v_price1),
        (v_bill_id, v_product2_id, v_qty2, v_price2);

    -- ========================================
    -- 7. Reducir el stock de los productos
    -- ========================================
    UPDATE products
    SET stock = stock - v_qty1
    WHERE product_id = v_product1_id;

    UPDATE products
    SET stock = stock - v_qty2
    WHERE product_id = v_product2_id;

    -- ========================================
    -- 8. Mensaje de éxito
    -- ========================================
    RAISE NOTICE '✅ Compra realizada con éxito. Factura ID: %, Total: %', v_bill_id, v_total;

EXCEPTION
    -- Si algo falla, se hace ROLLBACK automático y se muestra el error
    WHEN OTHERS THEN
        RAISE NOTICE '❌ Error en la transacción: %', SQLERRM;
        RAISE;  -- Vuelve a lanzar el error para que se vea claramente
END $$;