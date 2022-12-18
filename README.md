# What to eat

Course project for tsoha: I am always complaining about not knowing what to eat, so I came up with this solution.
How about a website that decides for me?

**Current features:**
* Generate a random meal from the database
* Submit a food by filling out a form
* Make an account, log in and out
* View your own profile page
  * A list of foods you have posted
  * A list of foods you have saved as favorite
* View list of all foods and each separately
* View list of all foods of chosen mealtype (Breakfast, Meal, Snack, Dessert)
* Vote if a food is good or bad
  * Current score rating can be seen from individual food pages (a good vote is +1 and a bad vote is -1 to the score)
* Save food as favorite (bugs: a food can be saved multiple times by each user)
* Comment on food pages and read comments left by others

**Installation:**
1. Clone repository onto your local device
2. Create virtual environment for the program in the same folder
```
python3 -m venv venv 
```
3. Activate the environment
```
source venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Create .env file and in the file `SECRET_KEY=` and `DATABASE_URL=` variables
6. Start postgresql database on another terminal tab
7. On the first tab run
```
psql < schema.sql
```
8. and finally start the program on the first tab by typing
```
flask run
```

**What would have been nice and other comments:**

* There is quite a lot of empty space on the right-hand side of all the pages, as I planned the design to also fit vertical screens.
* I do think this was a succesful project and I'll definitely be using the app, maybe even improving it in the future! I'd also like to publish this, as the app definitely works best with a community, where everyone can share their favorite meals. I'll update on that part once I, or the instructors for next year's course, find a free way to do that :D. Here are some of the features I had planned but didn't make it:

* Edit posts and comments
* Delete posts and comments
* Sort by cuisine/ price (estimate) / votes / time / diet
* If I had proper recipes, I would have liked to use a [Select2 dropdown menu](https://select2.org/getting-started/basic-usage) for adding ingredients
* Search by ingredient and name
* Exclude recipes that include specific ingredients (allergies)
* Exclude foods that are of a specific diet
* Adding measurements to ingredients when creating a recipe (1 or more carrots? 500 ml or 1 l of milk?)

(Disclaimer: not actual health advice, please consult a professional nutritionist/doctor if you have trouble eating)
