
-- "Компьютерная фирма"
-- https://www.sql-ex.ru/help/select13.php#db_1

-- Создание таблиц

CREATE TABLE Product
(
    maker char(10) NOT NULL,
    model char(50) NOT NULL,
    type char(50) NOT NULL
);

CREATE TABLE PC
(
    code int NOT NULL,
    model char(50) NOT NULL,
    speed int NOT NULL,
    ram int NOT NULL,
    hd decimal(3,1) NOT NULL,
    cd char(10) NOT NULL,
    price decimal(15,2)
);

CREATE TABLE Laptop
(
    code int NOT NULL,
    model char(50) NOT NULL,
    speed int NOT NULL,
    ram int NOT NULL,
    hd decimal(3,1) NOT NULL,
    price decimal(15,2),
    screen int NOT NULL
);

CREATE TABLE Printer
(
    code int NOT NULL,
    model char(50) NOT NULL,
    color char(1) NOT NULL,
    type char(10) NOT NULL,
    price decimal(15,2)
);


-- Primary keys

ALTER TABLE Product ADD PRIMARY KEY (model);
ALTER TABLE PC ADD PRIMARY KEY (code);
ALTER TABLE Laptop ADD PRIMARY KEY (code);
ALTER TABLE Printer ADD PRIMARY KEY (code);


-- Foreign keys

ALTER TABLE PC ADD CONSTRAINT FK_PC_model FOREIGN KEY (model) REFERENCES Product (model);
ALTER TABLE Laptop ADD CONSTRAINT FK_Laptop_model FOREIGN KEY (model) REFERENCES Product (model);
ALTER TABLE Printer ADD CONSTRAINT FK_Printer_model FOREIGN KEY (model) REFERENCES Product (model);


-- Заполнить таблицы данными

INSERT INTO Product (maker, model, type)
VALUES ('A', '1232', 'PC');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1233', 'PC');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1276', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1298', 'Laptop');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1401', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1408', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('A', '1752', 'Laptop');

INSERT INTO Product (maker, model, type)
VALUES ('B', '1121', 'PC');

INSERT INTO Product (maker, model, type)
VALUES ('B', '1750', 'Laptop');

INSERT INTO Product (maker, model, type)
VALUES ('C', '1321', 'Laptop');

INSERT INTO Product (maker, model, type)
VALUES ('D', '1288', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('D', '1433', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('E', '1260', 'PC');

INSERT INTO Product (maker, model, type)
VALUES ('E', '1434', 'Printer');

INSERT INTO Product (maker, model, type)
VALUES ('E', '2112', 'PC');

INSERT INTO Product (maker, model, type)
VALUES ('E', '2113', 'PC');


INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (1, '1232', 500, 64, 5.0, '12x', 600.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (10, '1260', 500, 32, 10.0, '12x', 350.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (11, '1233', 900, 128, 40.0, '40x', 980.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (12, '1233', 800, 128, 20.0, '50x', 970.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (2, '1121', 750, 128, 14.0, '40x', 850.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (3, '1233', 500, 64, 5.0, '12x', 600.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (4, '1121', 600, 128, 14.0, '40x', 850.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (5, '1121', 600, 128, 8.0, '40x', 850.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (6, '1233', 750, 128, 20.0, '50x', 950.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (7, '1232', 500, 32, 10.0, '12x', 400.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (8, '1232', 450, 64, 8.0, '24x', 350.0000);

INSERT INTO PC (code, model, speed, ram, hd, cd, price)
VALUES (9, '1232', 450, 32, 10.0, '24x', 350.0000);


INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (1, '1298', 350, 32, 4.0, 700.0000, 11);

INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (2, '1321', 500, 64, 8.0, 970.0000, 12);

INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (3, '1750', 750, 128, 12.0, 1200.0000, 14);

INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (4, '1298', 600, 64, 10.0, 1050.0000, 15);

INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (5, '1752', 750, 128, 10.0, 1150.0000, 14);

INSERT INTO Laptop (code, model, speed, ram, hd, price, screen)
VALUES (6, '1298', 450, 64, 10.0, 950.0000, 12);


INSERT INTO Printer (code, model, color, type, price)
VALUES (1, '1276', 'n', 'Laser', 400.0000);

INSERT INTO Printer (code, model, color, type, price)
VALUES (2, '1433', 'y', 'Jet', 270.0000);

INSERT INTO Printer (code, model, color, type, price)
VALUES (3, '1434', 'y', 'Jet', 290.0000);

INSERT INTO Printer (code, model, color, type, price)
VALUES (4, '1401', 'n', 'Matrix', 150.0000);

INSERT INTO Printer (code, model, color, type, price)
VALUES (5, '1408', 'n', 'Matrix', 270.0000);

INSERT INTO Printer (code, model, color, type, price)
VALUES (6, '1288', 'n', 'Laser', 400.0000);