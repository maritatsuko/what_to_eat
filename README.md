# What to eat

Course project for tsoha: I am always complaining about not knowing what to eat, so I came up with this solution.
How about a website that decides for me?

**Current features:**
* Generate a random meal from a list of recipes
* Make an account, log in and out
* Submit a recipe via form
* View list of all recipes and every recipe separately
* Vote if a recipe is good or bad
  * Current ratings can be seen from individual recipe pages (a good vote is +1 and a bad vote is -1)

**Ideas / things I'm working on:**
* Switching the new recipe form ingredient part from checkboxes to a Select2 dropdown menu
  * There's currently 2 placeholder ingredients. Realistically, the number of ingredient options available will be bigger, so there's no point in presenting them as checkboxes, as that would take up the whole page. Also, a "regular" dropdown menu would not work, as there are multiple ingredients in a recipe and finding them all would be challenging. However, integrating select2 into this project might be above my current skill level. In that case, it would most likely be best just to have a text field in the form, and save the whole ingredient-list as a string and not enable searching by ingredients.
* Adding a junction table to better handle recipe-ingredient relations
* Csfr verification

**(future) Features:**
* Save your favorite recipes (PRIORITY)
* After adding a recipe to the public list:
  * Edit your recipes
  * Delete your recipe
  * Delete a comment left on your recipe
* Search for recipes
  * Search by name (PRIORITY) / ingredient
  * Sort by type (PRIORITY) / cuisine / price (estimate) / votes / time
  * Sort by diet (vegan / dairy free etc.) (PRIORITY)
  * Exclude recipes that include specific ingredients (allergies)
* Comment on recipes and read comments left by others
  * Delete your comment
* Adding measurements to ingredients when creating a recipe (1 or more carrots? 500 ml or 1 l of milk?)

(Disclaimer: not actual health advice, please consult a professional nutritionist/doctor if you have trouble eating)
