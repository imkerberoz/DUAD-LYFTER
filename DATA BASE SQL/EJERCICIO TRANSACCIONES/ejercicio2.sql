-- =============================================
-- EJERCICIO 2: Transacción de Compra (versión mejorada)
-- Soporta cualquier cantidad de productos usando FOR LOOP
-- =============================================

-- =============================================
-- MAPA CONCEPTUAL DEL CÓDIGO (pasos principales):
-- =============================================

--
-- 1. Validar que el usuario existe
--    → Si el usuario no existe, se cancela toda la transacción.
--
-- 2. Validar el stock de TODOS los productos (primer bucle)
--    → Se recorre la lista de productos y se verifica que haya
--      suficiente existencia de cada uno ANTES de hacer cualquier cambio.
--    → Si algún producto no tiene stock suficiente, se cancela todo.
--
-- 3. Crear la factura
--    → Se inserta la factura con total temporal en 0 y se obtiene su ID.
--
-- 4. Procesar cada producto (segundo bucle)
--    → Por cada producto de la lista se hace:
--        a) Insertar el ítem en bill_items
--        b) Reducir el stock del producto
--        c) Acumular el subtotal al total de la factura
--
-- 5. Actualizar el total real de la factura
--    → Se guarda el total calculado en el paso anterior.
--
-- 6. Manejo de errores (EXCEPTION)
--    → Si ocurre cualquier error en los pasos anteriores,
--      se hace ROLLBACK automático (no se guarda nada).
--
-- ¿Por qué se usan dos bucles?
-- - El primer bucle solo VALIDA (no modifica datos).
-- - El segundo bucle ya MODIFICA (inserta y actualiza).
-- Esto garantiza que si falta stock de algún producto,
-- no se haya creado la factura ni se haya tocado el inventario.
--
-- =============================================

DO $$
DECLARE
    v_user_id   INTEGER := 1;          -- ID del usuario que compra
    v_bill_id   INTEGER;               -- Aquí se guardará el ID de la factura creada
    v_total     NUMERIC(10,2) := 0;    -- Acumulador del total de la factura
    r           RECORD;                -- Variable especial para recorrer cada producto del bucle
    v_stock     INTEGER;               -- Stock actual del producto que se está evaluando
    v_price     NUMERIC(10,2);         -- Precio actual del producto que se está evaluando
BEGIN
    -- =====================================================
    -- 1. Validar que el usuario existe
    -- =====================================================
    IF NOT EXISTS (SELECT 1 FROM users WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe', v_user_id;
    END IF;

    -- =====================================================
    -- 2. PRIMER BUCLE: Validar stock de TODOS los productos
    -- =====================================================
    FOR r IN 
        SELECT * FROM (VALUES
            (1, 2),   -- product_id = 1 (Laptop), cantidad = 2
            (2, 3)    -- product_id = 2 (Mouse),  cantidad = 3
            -- Para agregar más productos solo se añade otra línea aquí
        ) AS lista(product_id, quantity)
    LOOP
        -- Obtener stock y precio del producto actual
        SELECT stock, price 
        INTO v_stock, v_price
        FROM products
        WHERE product_id = r.product_id;

        -- Validar que el producto exista
        IF v_stock IS NULL THEN
            RAISE EXCEPTION 'El producto con ID % no existe', r.product_id;
        END IF;

        -- Validar que haya stock suficiente
        IF v_stock < r.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente del producto %. Disponible: %, Solicitado: %',
                r.product_id, v_stock, r.quantity;
        END IF;
    END LOOP;

    -- =====================================================
    -- 3. Insertar la factura (total temporal = 0)
    -- =====================================================
    INSERT INTO bills (user_id, total_amount, status)
    VALUES (v_user_id, 0, 'completed')
    RETURNING bill_id INTO v_bill_id;   -- Guardamos el ID generado de la factura

    -- =====================================================
    -- 4. SEGUNDO BUCLE: Insertar ítems + reducir stock + calcular total
    -- =====================================================
    FOR r IN 
        SELECT * FROM (VALUES
            (1, 2),   -- Misma lista de productos que en el primer bucle
            (2, 3)
        ) AS lista(product_id, quantity)
    LOOP
        -- Obtener el precio actual del producto
        SELECT price INTO v_price
        FROM products
        WHERE product_id = r.product_id;

        -- Insertar el ítem en bill_items
        INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
        VALUES (v_bill_id, r.product_id, r.quantity, v_price);

        -- Reducir el stock del producto
        UPDATE products
        SET stock = stock - r.quantity
        WHERE product_id = r.product_id;

        -- Acumular el subtotal al total general
        v_total := v_total + (v_price * r.quantity);
    END LOOP;

    -- =====================================================
    -- 5. Actualizar el total real de la factura
    -- =====================================================
    UPDATE bills
    SET total_amount = v_total
    WHERE bill_id = v_bill_id;

    -- =====================================================
    -- 6. Mensaje de éxito
    -- =====================================================
    RAISE NOTICE '✅ Compra realizada con éxito. Factura ID: %, Total: %', v_bill_id, v_total;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE '❌ Error en la transacción: %', SQLERRM;
        RAISE;   -- Vuelve a lanzar el error para que se vea claramente
END $$;


-- ¿Cómo funciona el bucle?
-- El FOR r IN ... LOOP hace lo siguiente:

-- Toma la primera fila de la lista y la guarda en r
-- Ejecuta todo el código que está dentro del LOOP
-- Toma la siguiente fila y la guarda en r
-- Vuelve a ejecutar el código del LOOP
-- Repite hasta que no haya más filas

-- Ejemplo visual:

-- Primera vuelta del bucle:
-- r.product_id = 1
-- r.quantity = 2
-- Se valida el stock de la Laptop

-- Segunda vuelta del bucle:
-- r.product_id = 2
-- r.quantity = 3
-- Se valida el stock del Mouse 
--