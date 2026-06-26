CREATE TABLE `Products`(
    `product_id` INT NOT NULL,
    `Code` VARCHAR(50) NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price (decimal)` DECIMAL(10, 2) NOT NULL,
    `Entry date` DATE NOT NULL,
    `Brand` VARCHAR(100) NOT NULL,
    `Stock available` INT NOT NULL,
    PRIMARY KEY(`product_id`)
);
ALTER TABLE
    `Products` ADD PRIMARY KEY(`Code`);
CREATE TABLE `Invoices`(
    `invoice_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` VARCHAR(50) NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` VARCHAR(150) NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `Invoice_Items`(
    `detail_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `quantity` INT NOT NULL,
    `unit_price` DECIMAL(8, 2) NOT NULL,
    `line_total` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Shopping_Cart`(
    `cart_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(150) NOT NULL
);
CREATE TABLE `Cart_Items`(
    `cart_item_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `quantity` INT NOT NULL
);
ALTER TABLE
    `Cart_Items` ADD CONSTRAINT `cart_items_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `Shopping_Cart`(`cart_id`);
ALTER TABLE
    `Invoice_Items` ADD CONSTRAINT `invoice_items_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `Invoices`(`invoice_id`);
ALTER TABLE
    `Invoice_Items` ADD CONSTRAINT `invoice_items_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `Products`(`product_id`);
ALTER TABLE
    `Cart_Items` ADD CONSTRAINT `cart_items_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `Products`(`product_id`);