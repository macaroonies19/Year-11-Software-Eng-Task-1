from functions import get_nutrition, calculate_totals

print("Welcome to the Nutrition API")
print("Enter food name or multiple foods separated by commas (example: egg, toast)")

food_input = input("Enter food items: ")

foods = [f.strip() for f in food_input.split(",")]

items = []

for food in foods:
    result = get_nutrition(food)

    if result:
        items.append(result)

        print("\nNutrition for:", result["name"])
        print("------------------------")
        print("Serving Size (g):", result["serving_size_g"])
        print("Fat (g):", result["fat_total_g"])
        print("Saturated Fat (g):", result["fat_saturated_g"])
        print("Sodium (mg):", result["sodium_mg"])
        print("Potassium (mg):", result["potassium_mg"])
        print("Cholesterol (mg):", result["cholesterol_mg"])
        print("Carbs (g):", result["carbohydrates_total_g"])
        print("Sugar (g):", result["sugar_g"])
        print("Fiber (g):", result["fiber_g"])

    else:
        print("No data found for", food)

if len(items) > 1:
    totals = calculate_totals(items)

    print("\nTotal Nutrition")
    print("----------------")
    print("Fat (g):", totals["fat"])
    print("Saturated Fat (g):", totals["saturated_fat"])
    print("Sodium (mg):", totals["sodium"])
    print("Potassium (mg):", totals["potassium"])
    print("Cholesterol (mg):", totals["cholesterol"])
    print("Carbs (g):", totals["carbs"])
    print("Sugar (g):", totals["sugar"])
    print("Fiber (g):", totals["fiber"])

    result = get_nutrition(food)
    
