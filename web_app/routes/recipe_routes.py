from flask import Blueprint, request, render_template

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipe")
def index():
    print("Recipe...")
    #return "Welcome Home"
    return render_template("recipe.html")
