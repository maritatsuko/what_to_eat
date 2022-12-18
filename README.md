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
5. Start postgresql database on another terminal tab
6. Start the program on the first tab
```
flask run
```

**To be added (maybe):**
* After adding a food to the public list:
  * Edit your posts
  * Delete your posts
* Comments
  * Delete your own comment
  * Delete a comment left on your post
* Search for foods
  * Search by name
  * Sort by price (estimate) / votes / time
  * Sort by diet (vegan / dairy free etc.)
  * Exclude foods that are of a specific diet

**What would have been nice and other comments:**

* Originally I wanted to have proper recipies for each food added, but I ended up changing to just smaller descriptions per food. Adding ingredients by using a form with select2, and modifying the data between the database and the form just seemed way too complicated for now. Personally, I do think this was a good problem to run into, as I had to come up with other ideas and let the project adapt throughout the development. Unfortunately, due to some personal issues, I had to leave a bunch of other features out. However, I do think this was still a succesful project and I'll definitely be using the app, maybe even improving it in the future! I'd also like to publish this, as the app definitely works best with a community, where everyone can share their favorite meals. I'll update on that part once I, or the instructors for next year's course, find a free way to do that :D. Here are some of the features I had planned but didn't make it:

* Sort by cuisine
* If I had proper recipes, I would have liked to use a [Select2 dropdown menu](https://select2.org/getting-started/basic-usage) for adding ingredients
* Search by ingredient
* Exclude recipes that include specific ingredients (allergies)
* Adding measurements to ingredients when creating a recipe (1 or more carrots? 500 ml or 1 l of milk?)

(Disclaimer: not actual health advice, please consult a professional nutritionist/doctor if you have trouble eating)
