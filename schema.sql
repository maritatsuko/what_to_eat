CREATE TABLE users {
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
};

CREATE TABLE types {
    id SERIAL PRIMARY KEY,
    name TEXT
};

CREATE TABLE recipes {
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    name TEXT,
    type TEXT REFERENCES types,
    time INTEGER,
    price TEXT
};

