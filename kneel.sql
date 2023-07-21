CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE Orders
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    metal_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    style_id INTEGER NOT NULL,
    FOREIGN KEY(metal_id) REFERENCES Metals(id)
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY,
    `carets` NUMERIC(3, 1) NOT NULL,
    `price` NUMERIC(6, 2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5, 2) NOT NULL
);

DROP TABLE Orders;

CREATE TABLE Orders
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    metalId INTEGER NOT NULL,
    sizeId INTEGER NOT NULL,
    styleId INTEGER NOT NULL,
    FOREIGN KEY(metalId) REFERENCES Metals(id)
);

INSERT INTO Metals (metal, price)
VALUES
    ('Gold', 1500.00),
    ('Silver', 25.50),
    ('Platinum', 1800.75);

INSERT INTO Styles (style, price)
VALUES
    ('Classic', 500.00),
    ('Modern', 600.00),
    ('Elegant', 550.00);

INSERT INTO Sizes (carets, price)
VALUES
    (0.5, 405.00),
    (0.75, 580.00),
    (1.0, 700.00);


INSERT INTO Orders (metal_id, size_id, style_id)
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (1, 3, 2),
    (2, 1, 3);

SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    m.metal,
    m.price
FROM Orders o
JOIN Metals m 
    ON m.id = o.metal_id;
