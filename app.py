from flask import Flask, render_template, request
from helpers import lookup, get_recipe_details

# Configure application
app = Flask(__name__)


# Define routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredients = request.form.get("input")
        quantity = request.form.get("quantity")
        resultSet = lookup(ingredients, quantity)

        if len(resultSet) == 0:
            return render_template("apology.html", message="No recipes found!")
        recipe_list = []
        for result in resultSet:
            recipe = {
                "image": result.get("image"),
                "id": result.get("id"),
                "title": result.get("title"),
            }
            recipe_list.append(recipe)
        return render_template("result.html", recipe=recipe_list)
    return render_template("index.html")


@app.route("/<int:recipe_id>")
def recipe_details(recipe_id):
    details = get_recipe_details(recipe_id)
    return render_template("recipe_details.html", recipe_details=details)
