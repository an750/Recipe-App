# test/recipe_test.py

import os 
import pytest
from app.recipe_service import get_recipes

# testing to ensure we can properly access the API and access necessary data
def test_get_recipes():
    results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    #recipe_results = [recipe for recipe in results["results"]]
    assert results[0]["title"] == "Smoked Salmon Pasta"
    assert results[0]["servings"] == 4
    assert results[0]["readyInMinutes"] == 45
    assert results[0]["nutrition"]["nutrients"][0]["amount"] == 473.939
    assert results[0]["aggregateLikes"] == 33




  


   # invalid_results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+OOPS", minimum_calories="hello", maximum_calories="hi", max_ready_time="hey")
   # assert invalid_results == None
