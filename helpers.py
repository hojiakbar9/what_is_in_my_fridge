import requests
import os
import logging

from dotenv import load_dotenv
from os.path import join, dirname


# Set up logging
logging.basicConfig(filename="error.log", level=logging.ERROR)


def lookup(ingredients, quantity):
    try:
        formatted_ingredients = format_ingredients(ingredients)
        checked_quantity = check_quantity(quantity)
        params = f"ingredients={formatted_ingredients}&number={checked_quantity}"
        url = construct_url("recipes/findByIngredients", params=params)

        response = requests.get(url)
        response.raise_for_status()

        result = response.json()
        return result
    except Exception as e:
        logging.error(f"Error in lookup function: {e}")
        raise LookupError("Failed to fetch recipes") from e


def get_recipe_details(id):
    try:
        if id is not None:
            url = construct_url(
                f"recipes/{id}/information", params="includeNutrition=false"
            )
            response = requests.get(url)
            response.raise_for_status()

            result = response.json()
            return result
        else:
            return None
    except Exception as e:
        logging.error(f"Error in get_recipe_details function: {e}")
        raise LookupError("Failed to fetch recipe details") from e


def format_ingredients(ingredients):
    try:
        if not ingredients:
            raise ValueError("Input cannot be empty!")

        # Remove leading and trailing whitespaces
        ingredient_stripped = ingredients.strip()

        # Remove commas
        ingredient_commas_removed = ingredient_stripped.replace(",", " ")

        # split using space
        ingredient_string = ingredient_commas_removed.split()

        # remove duplicates
        ingredient_string = list(set(ingredient_string))

        # join using comma and plus
        ingredient_string = ",+".join(ingredient_string)

        return ingredient_string
    except Exception as e:
        logging.error(f"Error in format_ingredients function: {e}")
        raise ValueError("Failed to format ingredients") from e


def check_quantity(number):
    try:
        default_quantity = 20
        upperBound = 100
        lowerBound = 1

        if not number.strip():
            return default_quantity
        else:
            number = int(number)

            if number > upperBound or number < lowerBound:
                raise ValueError("Invalid number of recipes")
            else:
                return number
    except ValueError as ve:
        logging.error(f"Error in check_quantity function: {ve}")
        raise ValueError("Invalid quantity format") from ve


def get_api_key():
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    return os.environ.get("API_KEY")


def construct_url(endpoint, params=None):
    api_key = get_api_key()
    base_url = "https://api.spoonacular.com"
    url = f"{base_url}/{endpoint}?apiKey={api_key}"

    if params:
        url += f"&{params}"

    return url
