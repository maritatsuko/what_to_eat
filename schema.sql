CREATE TABLE users {
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
};

CREATE TABLE types {
    id SERIAL PRIMARY KEY,
    name TEXT
};

CREATE TABLE diets {
    id SERIAL PRIMARY KEY,
    name TEXT
};

CREATE TABLE ingredients {
    id SERIAL PRIMARY KEY,
    name TEXT,
    restriction REFERENCES diets,
};

CREATE TABLE recipes {
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    name TEXT UNIQUE,
    type TEXT REFERENCES types,
    cooktime INTEGER,
    price TEXT,
    ingredient REFERENCES ingredients,
    instructions TEXT,
};

