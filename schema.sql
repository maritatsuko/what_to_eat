CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE types (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE diets (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT,
    restriction INTEGER REFERENCES diets
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    name TEXT UNIQUE,
    type INTEGER REFERENCES types,
    cooktime INTEGER,
    price TEXT,
    ingredient TEXT,
    instructions TEXT
);
