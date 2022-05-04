from flask import Blueprint, request, render_template, jsonify
from app.recipe_service import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipe/form")
def recipe_form():
    print("RECIPE FORM...")
    return render_template("recipe_form.html")


@recipe_routes.route("/recipe", methods=["GET", "POST"])
def index():
    print("Recipe...")
    #return "Welcome Home"
    results = get_recipes(type_of_meal="pasta", final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    recipe_results = [recipe for recipe in results["results"]]
    if recipe_results:
        return render_template("recipe.html", results=recipe_results)
    else:
        return jsonify({"message": "Please try again."}), 404

