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
    # recipe_results = get_recipes(type_of_meal="pasta", final_ingreds="pasta+salmon", minimum_calories="200", maximum_calories="1000", max_ready_time="60")
    # if recipe_results:
    #     return render_template("recipe.html", results=recipe_results)
    # else:
    #     return jsonify({"message": "Please try again."}), 404

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST":  # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    type_of_meal = request_data.get("type_of_meal")
    final_ingreds = request_data.get("final_ingreds")
    minimum_calories = request_data.get("minimum_calories")
    maximum_calories = request_data.get("maximum_calories")
    max_ready_time = request_data.get("max_ready_time")

    recipe_results = get_recipes(type_of_meal=type_of_meal, final_ingreds=final_ingreds, minimum_calories=minimum_calories, maximum_calories=maximum_calories, max_ready_time=max_ready_time)
    if recipe_results:
        # flash("Plates Found!", "success")
        return render_template("recipe.html", results=recipe_results)
    else:
        # flash("No Plates Found. Please try again!", "danger")
        return jsonify({"message": "Please try again."}), 404
