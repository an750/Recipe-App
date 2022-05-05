# test/recipe_test.py

import os 
import pytest

from app.recipe_service import get_recipes

def test_get_recipes():
    results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    assert results["type_of_meal"] == "pasta"
    assert results["final_ingreds"] == "pasta+salmon"
    assert results["minimum_calories"]


    invalid_results = get_recipes(type_of_meal="pasta",final_ingreds="pasta+OOPS", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    assert invalid_results == None
