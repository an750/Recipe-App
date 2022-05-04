#recipe app code from Collab

import requests
import json
from pprint import pprint
# from IPython.display import Image, display #isn't recongized- is this only a Collab thing
from operator import itemgetter

#headers = {"...": API_KEY}
#response= requests.get(url, header=headers)

# user inputs: 
# type_of_meal = input("What are you in the mood for today?: ")
# ingred_on_hand_str = input("What ingredients do you have on hand? ") 
# ingred_on_hand_list = ingred_on_hand_str.split(", ")
# final_ingreds= ""
# for ingred in ingred_on_hand_list: 
#   final_ingreds += ingred+"+"
# print("What is your ideal range of calories per serving?")
# minimum_calories = int(input("Min Calories: "))
# maximum_calories = int(input("Max Calories: "))
# max_ready_time = int(input("What is the maximum time in minutes you wish to spend cooking?:"))
# print("---------------")

  # USER-PROVIDED : query, includeIngredients, minCalories, maxCalories, MaxReadyTime
  # DEFAULTS (hardcoded) : addRecipeInformation=True, sort=popularity, number=10, apiKey="b3279262707c4e28bada553971c1b62a"

def get_recipes(type_of_meal, final_ingreds, minimum_calories, maximum_calories, max_ready_time):
    # API_KEY = "b3279262707c4e28bada553971c1b62a" # todo: use env vars
    API_KEY = "7c8d9e352ee44612ac9285bcd1d591b1"
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={type_of_meal}&includeIngredients={final_ingreds}&minCalories={minimum_calories}&maxCalories={maximum_calories}&maxReadyTime={max_ready_time}&addRecipeInformation=True&sort=popularity&number=5&apiKey={API_KEY}" # url with user input variables
    response = requests.get(url)
    recipe_search_data = json.loads(response.text)
<<<<<<< HEAD
=======
    #pprint(recipe_search_data)
>>>>>>> 7681c1b684b975c58bc19c53ed6bc8c506347110
    return recipe_search_data

# need to change this hard coded variables to dynamic user inputs
if __name__ == "__main__":
    recipe_search_data = get_recipes(type_of_meal="pasta",final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    recipe_results = [recipe for recipe in recipe_search_data["results"]]
    for recipe in recipe_results:
        print(recipe["title"])
        print("Likes:", recipe["aggregateLikes"])
        print("Total Preparation Time:", recipe["readyInMinutes"],"minutes")
        print("Calories:", round((recipe["nutrition"]["nutrients"][0]["amount"])))
        print("Servings:", recipe["servings"])
        print("See Detailed Recipe Info:", recipe["spoonacularSourceUrl"])
        # display(Image(url=recipe["image"])) # needs fixing: displays picture of meal


