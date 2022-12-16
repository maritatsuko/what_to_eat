# What to eat

Course project for tsoha: I am always complaining about not knowing what to eat, so I came up with this solution.
How about a website that decides for me?

**Current features:**
* Generate a random meal from the database
* Make an account, log in and out
* Submit a food by filling out a form
* View your own profile page
  * A list of foods you have posted
  * A list of foods you have saved as favorite (bugs: does not show recipe names)
* View list of all foods and each separately
* View list of all foods of chosen mealtype (Breakfast, Meal, Snack, Dessert)
* Vote if a food is good or bad
  * Current ratings can be seen from individual food pages (a good vote is +1 and a bad vote is -1)
* Save food as favorite (bugs: can save same food multiple times)
* Comment on food pages and read comments left by others (change user number to username)

**Comments:**
* Currently the foods have been changed from recipes to just ideas with small descriptions. Having proper recipes on the actual site would be ideal, but reducing it to something less complicated is still following the main vision. That is, to simply give ideas when not wanting to make decisions.

* If I had proper recipes, I would have liked to switch the new recipe form ingredient part from checkboxes to a [Select2 dropdown menu](https://select2.org/getting-started/basic-usage)
  * There were only 2 placeholder ingredients before. Realistically, the number of ingredient options available would be bigger, so there's would be no point in presenting them as checkboxes, as that would have taken the whole page. Also, a "regular" dropdown menu would've not worked, as there are multiple ingredients per recipe and finding them all would've been too challenging and not user-friendly. However, integrating select2 into this project might have been above my current skill level and as this is a course project, it would have taken me too much time.
  [test3.html](templates/test3.html) has an simplified example of the select2 approach.
  * Adding a junction table to better handle recipe-ingredient relations


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
  * Sort by diet (vegan / dairy free etc.) (PRIORITY)
  * Exclude foods that are of a specific diet
* A more eyepleasing user interface (PRIORITY)

**What would have been nice:**
* Search by ingredient
* Exclude recipes that include specific ingredients (allergies)
* Sort by cuisine
* Adding measurements to ingredients when creating a recipe (1 or more carrots? 500 ml or 1 l of milk?)

(Disclaimer: not actual health advice, please consult a professional nutritionist/doctor if you have trouble eating)
