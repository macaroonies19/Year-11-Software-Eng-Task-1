import requests
import pandas as pd

API_KEY = "LY1OdRo80RFWhX3bg8ddfhrnuYia3LSXmXc9YTcY"

def get_nutrition(food):
    """
    Fetch nutrition data for a given food using the API Ninjas Nutrition API.
    Returns a dictionary or None if no data is found.
    """

    url = "https://api.api-ninjas.com/v1/nutrition"
    headers = {"X-Api-Key": API_KEY}
    params = {"query": food}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)

        # Handle HTTP errors
        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        return data[0]

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
        return None

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the API.")
        return None


def calculate_totals(items):
    """
    Takes a list of nutrition dictionaries and returns total values.
    """

    totals = {
        "fat": 0,
        "saturated_fat": 0,
        "sodium": 0,
        "potassium": 0,
        "cholesterol": 0,
        "carbs": 0,
        "sugar": 0,
        "fiber": 0
    }

    for item in items:
        totals["fat"] += item.get("fat_total_g", 0)
        totals["saturated_fat"] += item.get("fat_saturated_g", 0)
        totals["sodium"] += item.get("sodium_mg", 0)
        totals["potassium"] += item.get("potassium_mg", 0)
        totals["cholesterol"] += item.get("cholesterol_mg", 0)
        totals["carbs"] += item.get("carbohydrates_total_g", 0)
        totals["sugar"] += item.get("sugar_g", 0)
        totals["fiber"] += item.get("fiber_g", 0)

    return totals
