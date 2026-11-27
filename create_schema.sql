CREATE TABLE IF NOT EXISTS Book (
    bookID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publisher TEXT NOT NULL,
    year INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_price REAL NOT NULL,
    rent_price REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS Customer (
    customerID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    type TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Sale (
    saleID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID INTEGER NOT NULL,
    bookID INTEGER NOT NULL,
    saleDate TEXT NOT NULL,
    totalPrice REAL NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (bookID) REFERENCES Book(bookID)
);
CREATE TABLE IF NOT EXISTS Rental (
    rentalID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID INTEGER NOT NULL,
    bookID INTEGER NOT NULL,
    rentDate TEXT NOT NULL,
    dueDate TEXT NOT NULL,
    status TEXT NOT NULL,
    totalPrice REAL NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (bookID) REFERENCES Book(bookID)
);