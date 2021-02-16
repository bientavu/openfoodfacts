DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category (
    id INT NOT NULL AUTO_INCREMENT,
    name_cat VARCHAR(40) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Product;
CREATE TABLE IF NOT EXISTS Product (
    id INT NOT NULL AUTO_INCREMENT,
    name_product VARCHAR(100) NOT NULL,
    category_fk INT NOT NULL,
    store VARCHAR(45) NOT NULL,
    nutriscore VARCHAR(1) NOT NULL,
    link TEXT,
    PRIMARY KEY (id),
    CONSTRAINT fk_category_idcategory
        FOREIGN KEY (category_fk)
        REFERENCES Category(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Substitute;
CREATE TABLE IF NOT EXISTS Substitute (
    id INT NOT NULL AUTO_INCREMENT,
    id_product_to_substitute INT NOT NULL,
    id_product_substitute INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_idproducttosubstitute_idproduct
        FOREIGN KEY (id_product_to_substitute)
        REFERENCES Product(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_idproductsubstitute_idproduct
        FOREIGN KEY (id_product_substitute)
        REFERENCES Product(id) ON DELETE CASCADE ON UPDATE CASCADE
)

ENGINE=INNODB;