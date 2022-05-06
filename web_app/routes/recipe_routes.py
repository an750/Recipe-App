# web_app/routes/recipe_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash
from app.recipe_service import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipe/form")
def recipe_form():
    print("RECIPE FORM...")
    return render_template("recipe_form.html")

#route gets user inputs from recipe/form as dynamic parameters and calls the get_recipes() function to access and return recipes from the API
@recipe_routes.route("/recipe", methods=["GET", "POST"])
def index():
    print("Recipe...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST":  # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    type_of_meal = request_data.get("type_of_meal") or "food"
    final_ingreds = request_data.get("final_ingreds") or "-"
    minimum_calories = request_data.get("minimum_calories") or 1
    maximum_calories = request_data.get("maximum_calories") or 10000
    max_ready_time = request_data.get("max_ready_time") or 10000

    # load error message page for invalid non-integer inputs for integer parameters
    if int(isinstance(minimum_calories,int)) == False:
        return render_template("no_recipe.html")
    elif int(isinstance(maximum_calories,int)) == False:
        return render_template("no_recipe.html")
    elif int(isinstance(max_ready_time,int)) == False: 
        return render_template("no_recipe.html")  
   
    # call get_recipes function with form inputs as parameteres
    recipe_results = get_recipes(type_of_meal=type_of_meal, final_ingreds=final_ingreds, minimum_calories=minimum_calories, maximum_calories=maximum_calories, max_ready_time=max_ready_time)
    
    # render the recipe results page if successful and alert the user
    if recipe_results:
        flash("Plates Found!", "success")
        return render_template("recipe.html", results=recipe_results)
    else:
        flash("No Plates Found. Please try again!", "danger")
        return render_template("no_recipe.html")
