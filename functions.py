import requests
import pandas as pd
import matplotlib.pyplot as plt

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

def graph_single_food(item):
    """
    Creates a bar chart for a single food item.
    """

    labels = ["Fat", "Carbs", "Sugar", "Fiber"]
    values = [
        item["fat_total_g"],
        item["carbohydrates_total_g"],
        item["sugar_g"],
        item["fiber_g"]
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=["#ff9999", "#99ccff", "#ffcc99", "#c2f0c2"])
    plt.title(f"Nutrition Breakdown for {item['name']}")
    plt.ylabel("Grams (g)")
    plt.show()


def graph_multiple_foods(items):
    """
    Creates a stacked bar chart comparing multiple foods.
    """

    names = [item["name"] for item in items]

    fat = [item["fat_total_g"] for item in items]
    carbs = [item["carbohydrates_total_g"] for item in items]
    sugar = [item["sugar_g"] for item in items]

    plt.figure(figsize=(10, 6))

    plt.bar(names, fat, label="Fat")
    plt.bar(names, carbs, bottom=fat, label="Carbs")
    plt.bar(names, sugar, bottom=[fat[i] + carbs[i] for i in range(len(items))], label="Sugar")

    plt.title("Nutrition Comparison")
    plt.ylabel("Grams (g)")
    plt.legend()
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
