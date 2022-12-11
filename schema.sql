CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TYPE mealtype AS ENUM ('Breakfast', 'Meal', 'Snack', 'Dessert');

CREATE TYPE diets AS ENUM ('Vegan', 'Gluten free', 'No dairy', 'Meat', 'Fish');

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    name TEXT UNIQUE,
    type mealtype,
    cooktime INTEGER,
    price TEXT,
    description VARCHAR(300),
    diet TEXT[]
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    creator INTEGER REFERENCES users,
    recipe INTEGER REFERENCES recipes,
    comment TEXT
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    recipe_id INTEGER REFERENCES recipes,
    vote INTEGER
);

CREATE TABLE favorites (
    user_id INTEGER REFERENCES users,
    recipe_id INTEGER REFERENCES recipes,
    favorite BOOLEAN
);