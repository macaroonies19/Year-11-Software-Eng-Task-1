from functions import (
    get_nutrition,
    calculate_totals,
    graph_single_food,
    graph_multiple_foods
)
import pandas as pd


# DataFrame to store user interactions
history = pd.DataFrame(columns=["food", "fat", "carbs", "sugar"])


def show_help():
    print("\nHELP MENU")
    print("1. Enter food names separated by commas (e.g., egg, toast)")
    print("2. Type 'history' to view past searches")
    print("3. Type 'exit' to quit the program")
    print("4. Type 'help' to view this menu again\n")


def display_nutrition(result):
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


def main():
    print("Welcome to the Nutrition API")
    print("Type 'help' for instructions.\n")

    while True:
        user_input = input("Enter food items: ").strip().lower()

        # Exit program
        if user_input == "exit":
            print("Goodbye!")
            break

        # Help menu
        if user_input == "help":
            show_help()
            continue

        # Show history
        if user_input == "history":
            print("\n--- Past Interactions ---")
            print(history if not history.empty else "No history yet.")
            print()
            continue

        # Empty input
        if not user_input:
            print("Error: You must enter at least one food name.\n")
            continue

        # Split foods
        foods = [f.strip() for f in user_input.split(",")]
        items = []

        # Process each food
        for food in foods:
            result = get_nutrition(food)

            if result:
                display_nutrition(result)
                items.append(result)

                # Add to history DataFrame
                history.loc[len(history)] = [
                    result["name"],
                    result["fat_total_g"],
                    result["carbohydrates_total_g"],
                    result["sugar_g"]
                ]

            else:
                print(f"No data found for '{food}'. Check spelling.\n")

        # Show totals if multiple foods
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
            print()

        # Ask user if they want a graph
        while True:
            graph_choice = input("Show graph? (yes/no): ").strip().lower()

            if graph_choice == "yes":
                if len(items) == 1:
                    graph_single_food(items[0])
                else:
                    graph_multiple_foods(items)
                break

            elif graph_choice == "no":
                break

            else:
                print("Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
