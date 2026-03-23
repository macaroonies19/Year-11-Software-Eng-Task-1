import requests

API_KEY = "LY1OdRo80RFWhX3bg8ddfhrnuYia3LSXmXc9YTcY"

def get_nutrition(food):
    url = "https://api.api-ninjas.com/v1/nutrition"

    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "query": food
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            return None
        return data[0]
    else:
        return None


def calculate_totals(items):
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
        totals["fat"] += item["fat_total_g"]
        totals["saturated_fat"] += item["fat_saturated_g"]
        totals["sodium"] += item["sodium_mg"]
        totals["potassium"] += item["potassium_mg"]
        totals["cholesterol"] += item["cholesterol_mg"]
        totals["carbs"] += item["carbohydrates_total_g"]
        totals["sugar"] += item["sugar_g"]
        totals["fiber"] += item["fiber_g"]

    return totals


