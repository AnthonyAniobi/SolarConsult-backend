# Intercontinental Food Recipes

This project helps you find recipes for foods from several parts of the world. You specify your taste both in type and health requirements and the food is provided with the recipe.
The project is based on the [edemon](www.edemam.com) api.

The project is hosted [here checkout the current state of the app](https://intercontinental-recipes.web.app/)

### How to use
- Open the website
- Search food from the search form
- Choose your preference
    the preferences available are:
    'vegetarian', 'alcohol-free',
    'immuno-supportive', 'celery-free', 'crustacean-free',
    'diary-free', 'egg-free', 'fish-free', 'fodmap-free',
    'gluten-free', 'keto-friendly', 'kidney-friendly',
    'kosher', 'low-potassium', 'lupine-free',
    'mustard-free', 'low-fat-abs', 'No-oil-added',
    'low-sugar', 'paleo', 'peanut-free',
    'pecatarian', 'pork-free', 'vegan',
- Click on Get Recipe to get a list of recipes matching your request

### Screenshots
![Home Page](screenshots/intercontinentalRecipe.png)


### Setting Up
To have this project up and running on your machine you would have to set the environment vaiables. You can do this by following the process below
1. Sign up at [Edemam](www.edemam.com)
2. Get your app id and api key
3. clone a local copy of this project on your machine
4. run `npm install` to get all modules
5. Create a `.env` file in the root directory
6. Add your app id and api key in the `.env` file as shown below:
    ```
    REACT_APP_APP_KEY = "615ec659220c9191b68e363c8615cc3c"
    REACT_APP_APP_ID = "6e031aee"
    ```
7. Start the project using `npm start`
8. You can now search for recipes from all arround the world