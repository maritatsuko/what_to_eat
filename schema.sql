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
    restriction REFERENCES diet
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    creator TEXT REFERENCES users,
    name TEXT UNIQUE,
    type TEXT REFERENCES types,
    cooktime INTEGER,
    price TEXT,
    ingredient LIST REFERENCES ingredients,
    instructions TEXT,
);
