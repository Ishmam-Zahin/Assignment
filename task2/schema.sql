CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) UNIQUE,
    release_date VARCHAR(20),
    display_size NUMERIC(3,1),
    display_width INTEGER,
    display_height INTEGER,
    battery INTEGER,
    camera INTEGER,
    ram INTEGER,
    storage INTEGER,
    price NUMERIC(8,2)
);
