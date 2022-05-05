# test/recipe_test.py

import os 
import pytest

from app.recipe_service import get_recipes

def test_get_recipes():
    results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    recipe_results = [recipe for recipe in results["results"]]
    assert recipe_results[0]["type_of_meal"] == "pasta"
    assert recipe_results[0]["final_ingreds"] == "pasta+salmon"
    assert recipe_results[0]["minimum_calories"] == "200"
    assert recipe_results[0]["maximum_calories"] == "1000"
    assert recipe_results[0]["max_ready_time"] == "60"


    invalid_results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+OOPS", minimum_calories="hello", maximum_calories="hi", max_ready_time="hey")
    assert invalid_results == None
