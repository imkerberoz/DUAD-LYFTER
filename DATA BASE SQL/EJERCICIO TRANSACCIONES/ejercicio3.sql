-- =============================================
-- EJERCICIO 3: Transacción de Retorno de Productos
-- =============================================

DO $$
DECLARE
    v_bill_id INTEGER := 1;              -- ID de la factura que se va a devolver
    v_existe BOOLEAN;                    -- Para verificar si la factura existe
BEGIN
    -- ========================================
    -- 1. Verificar que la factura existe
    -- ========================================
    SELECT EXISTS(
        SELECT 1 FROM bills WHERE bill_id = v_bill_id
    ) INTO v_existe;

    IF NOT v_existe THEN
        RAISE EXCEPTION 'La factura con ID % no existe', v_bill_id;
    END IF;

    -- ========================================
    -- 2. Aumentar el stock de los productos
    --    (según lo que se compró en esa factura)
    -- ========================================
    UPDATE products p
    SET stock = p.stock + bi.quantity
    FROM bill_items bi
    WHERE bi.bill_id = v_bill_id
      AND p.product_id = bi.product_id;

    -- ========================================
    -- 3. Marcar la factura como "Retornada"
    -- ========================================
    UPDATE bills
    SET status = 'returned'
    WHERE bill_id = v_bill_id;

    -- ========================================
    -- 4. Mensaje de éxito
    -- ========================================
    RAISE NOTICE '✅ Devolución realizada con éxito. Factura ID: % marcada como Retornada', v_bill_id;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE '❌ Error en la devolución: %', SQLERRM;
        RAISE;
END $$;