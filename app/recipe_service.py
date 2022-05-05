#recipe app code from Collab
import os 
from dotenv import load_dotenv
import requests
import json
from pprint import pprint
# from IPython.display import Image, display #isn't recongized- is this only a Collab thing
from operator import itemgetter

load_dotenv()
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_recipes(type_of_meal, final_ingreds, minimum_calories, maximum_calories, max_ready_time):
    SPOONACULAR_API_KEY = "be052ff238974959a8fb9b773d179250" # todo: use env vars
    # # API_KEY = "7c8d9e352ee44612ac9285bcd1d591b1"
    # # API_KEY = "c174b3169b224fd18bef932852107915"
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={type_of_meal}&includeIngredients={final_ingreds}&minCalories={minimum_calories}&maxCalories={maximum_calories}&maxReadyTime={max_ready_time}&addRecipeInformation=True&sort=popularity&number=10&apiKey={SPOONACULAR_API_KEY}" # url with user input variables
    response = requests.get(url)
    recipe_search_data = json.loads(response.text)
    recipe_results = [recipe for recipe in recipe_search_data["results"]]
    # pprint(recipe_results[0])
    return recipe_results

# need to change this hard coded variables to dynamic user inputs
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


