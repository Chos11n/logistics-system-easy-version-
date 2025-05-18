-- database/schema.sql
CREATE TABLE goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    manufacturer TEXT,
    quantity INTEGER,
    volume REAL,
    weight REAL,
    notes TEXT,
    date TEXT -- ISO格式 YYYY-MM-DD
);
