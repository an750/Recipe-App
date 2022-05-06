#recipe app code from Collab
import os 
from dotenv import load_dotenv
import requests
import json
from pprint import pprint
from operator import itemgetter

load_dotenv()
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_recipes(type_of_meal, final_ingreds, minimum_calories, maximum_calories, max_ready_time):
    """
    Fetches recipes from Spoonacular API given desired type of meal, ingredients, number of calories, and max prep time.

    Params:
    type_of_meal (str) the type of meal recipe, like “pasta”
    final_ingreds (str) desired ingredients in the recipe, like “chicken” or “chicken+cheese”
    minimum_calories (int) desired minimum calories in the recipe, like “200”
    maximum_calories (int) desired maximum calories in the recipe, like “1000"
    max_ready_time (str) desired maximum preparation time in minutes, like “60”

    Example:
    get recipe(type_of_meal=“pasta”, final_ingreds=“chicken+cheese”, minimum_calories=“200", maximum_calories=“1000”, max_ready_time=“60")

    Returns a list of dictionaries corresponding to various recipes given parameters

    Spoonacular Documentation: https://spoonacular.com/food-api/docs#Search-Recipes-Complex

    """
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={type_of_meal}&includeIngredients={final_ingreds}&minCalories={minimum_calories}&maxCalories={maximum_calories}&maxReadyTime={max_ready_time}&addRecipeInformation=True&sort=popularity&number=10&apiKey={SPOONACULAR_API_KEY}" # url with user input variables
    response = requests.get(url)
    recipe_search_data = json.loads(response.text)
    recipe_results = [recipe for recipe in recipe_search_data["results"]]
    # pprint(recipe_results[0])
    return recipe_results

# for local testing of the app function
if __name__ == "__main__":
    recipe_search_data = get_recipes(type_of_meal="pasta",final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    for recipe in recipe_search_data:
        print(recipe["title"])
        print("Likes:", recipe["aggregateLikes"])
        print("Total Preparation Time:", recipe["readyInMinutes"],"minutes")
        print("Calories:", round((recipe["nutrition"]["nutrients"][0]["amount"])))
        print("Servings:", recipe["servings"])
        print("See Detailed Recipe Info:", recipe["spoonacularSourceUrl"])
        # display(Image(url=recipe["image"]))


