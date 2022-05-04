from flask import Blueprint, request, render_template
from app.recipe_service import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipe")
def index():
    print("Recipe...")
    #return "Welcome Home"
    results = get_recipes()
    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "Please try again."}), 404
    return render_template("recipe.html")
