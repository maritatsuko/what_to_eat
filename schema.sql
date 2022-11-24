CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TYPE mealtype AS ENUM ('Breakfast', 'Meal', 'Snack', 'Dessert');

CREATE TYPE diets AS ENUM ('Vegan', 'Gluten free', 'No dairy', 'Meat', 'Fish');

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT,
    restriction diets
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    name TEXT UNIQUE,
    type mealtype,
    cooktime INTEGER,
    price TEXT,
    instructions TEXT,
    ingredient TEXT[]
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    recipe INTEGER REFERENCES recipes,
    comment TEXT
);
