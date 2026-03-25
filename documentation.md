# Requirements Definition
## Functional Requirements
### Data Retrieval:
The system must be able to:
- Accept one or multiple food names from the user.
- Retrieve nutrition data for each food using the API Ninjas Nutrition API.
- Handle cases where the API returns no results (e.g., misspelled or unknown foods).
- Handle API errors such as timeouts or connection failures.
- Retrieve key nutrition fields including: fats, sugar, carbs.

### User Interface
The system must:
- Provide a simple text‑based interface.
- Allow the user to: Enter food names, view help instructions, view past interactions, exit the program.
- Accept input regardless of upper/lower case.
- alidate user input and prevent crashes.
- Ask the user if they want to generate a graph after showing nutrition results.

### Data Display
The system must:
- Display nutrition information clearly for each food item.
- Display total nutrition values when multiple foods are entered.
- Show past user interactions stored during the session.
- Generate graphs using Matplotlib: Bar chart for a single food, stacked bar chart for multiple foods.
- Display clear error messages when: Input is empty, API returns no data, API request fails.

### Summary
| Requirement | Description | Verifiable |
| --- | --- | --- |
| FR1 | Accept one or multiple food names as input | Yes |
| FR2 | Retrieve nutrition data from an external API | Yes |
| FR3 | Validate user input and handle errors | Yes |
| FR4 | Display nutrition information clearly | Yes |
| FR5 | Calculate total nutrition for multiple foods | Yes |
| FR6 | Store user interactions during runtime | Yes |
| FR7 | Display past interactions on request | Yes |
| FR8 | Generate graphs using Matplotlib | Yes |
| FR9 | Allow the user to exit safely | Yes |
| FR10 | Provide a help menu | Yes |

# Determining Specifications
## Specification Table
| Feature | Input | Process | Output |
| --- | --- | --- | --- |
| Food search | Food name(s) | API request | Nutrition data |
| Multiple food totals | List of foods | Sum nutrition values | Total nutrition |
| History tracking | Successful search | Append to DataFrame | History table |
| Graphing | User chooses “yes” | Matplotlib renders chart | Bar/stacked graph |
| Help menu | "help" | Display instructions | Help text |
| Exit | "exit" | End program | Program closes |

## Use Cases
### Use Case 1 — Search for a Single Food
- Actors: User, Nutrition API
- Preconditions: The program is running, The user has access to the input prompt, The API key is valid and the API service is available.

- Main Flow:
1. User enters a single food name (e.g., “banana”).
2. System sends a request to the Nutrition API.
3. API returns nutrition data for the food.
4. System displays the nutrition information clearly.
5. System asks the user if they want to generate a graph.
6. If the user selects “yes”, a bar chart is displayed.
7. The interaction is saved to the session history.
- Alternative Flows:
1. API returns no data: User enters a food name, API returns an empty response, system displays: “No data found for ‘food’. Check spelling.”, system returns to the main menu.
2. API request fails: API times out or connection fails, system displays an error message, system returns to the main menu.
3. User enters invalid input: User enters an empty string or only spaces, system displays: “Error: You must enter at least one food name.”, system returns to the main menu.
- Postconditions: Nutrition data is displayed (if available), the food entry is added to the history DataFrame, the user is returned to the main input prompt.


### Use Case 2 — Search for Multiple Foods
- Actors: User, Nutrition API
- Preconditions: Program is running, user can enter input, API is available.

- Main Flow:
1. User enters multiple foods separated by commas (e.g., “egg, toast, banana”).
2. System splits the input into individual food names.
3. System sends an API request for each food.
4. System displays nutrition data for each food.
5. System calculates total nutrition values.
6. System displays the total nutrition table.
7. System asks if the user wants to generate a graph.
8. If “yes”, a stacked bar chart is displayed.
9. All valid foods are added to the history.
- Alternative Flows:
1. One or more foods return no data: API returns empty data for a food, system displays an error for that food only, system continues processing the remaining foods.
2. API request fails, API times out or fails, system displays an error message, system returns to the main menu.
- Postconditions: Nutrition data is displayed, totals are calculated, valid foods are stored in history, user returns to the main menu.

### Use Case 3 — View History
- Actors: User
- Preconditions: Program is running, at least one food has been searched (optional).

- Main Flow:
1. User types “history”.
2. System retrieves the DataFrame containing past interactions.
3. System displays the history table.
4. User returns to the main menu.
- Alternative Flows:
1. No history available: User types “history”, system detects an empty DataFrame, system displays “No history yet.”
- Postconditions: History is displayed (or message shown), user returns to main input prompt.

### Use Case 4 — View Help Menu
- Actors: User
- Preconditions: Program is running.

- Main Flow:
1. User types “help”.
2. System displays instructions on how to use the program.
3. System returns to the main menu.
- Alternative Flows: None

- Postconditions: Help information is shown, user returns to main input prompt.

### Use Case 5 — Exit the Program
- Actors: User
- Preconditions: Program is running.

- Main Flow:
1. User types “exit”.
2. System prints a goodbye message.
3. Program terminates safely without errors.
- Alternative Flows: None

- Postconditions: Program is closed.

### Use Case 6 — Generate Graph for a Single Food
- Actors: User, Matplotlib
- Preconditions: User has searched for one food, nutrition data is available.

- Main Flow:
1. System asks: “Show graph? (yes/no)”.
2. User types “yes”.
3. System prepares nutrition values (fat, carbs, sugar, fiber).
4. System generates a bar chart using Matplotlib.
5. Graph is displayed to the user.
- Alternative Flows:
1. User types “no”: System skips graph generation, returns to main menu.
- Postconditions: Graph is displayed (if chosen), user returns to main menu.

### Use Case 7 — Generate Graph for Multiple Foods
- Actors: User, Matplotlib
- Preconditions: User has searched for multiple foods, Nutrition data for all valid foods is available.

- Main Flow:
1. System asks: “Show graph? (yes/no)”.
2. User types “yes”.
3. System prepares nutrition values for each food.
4. System generates a stacked bar chart comparing foods.
5. Graph is displayed to the user.
- Alternative Flows:
1. User types “no”: System skips graph generation, returns to main menu.
- Postconditions: Graph is displayed (if chosen), user returns to main menu.

## Non‑Functional Specifications
### User Perspective
- Interface must be simple and easy to understand
- Program should respond within 1–3 seconds
- Error messages must be clear
- Graphs must be readable and labelled
### Developer Perspective
- Code must be modular and commented
- External dependencies listed in requirements.txt
- Program must run consistently across machines

# Design
## Data Dictionary
| Variable | Type | Description |
| --- | --- | --- |
| ``food`` | string | User‑entered food name |
| ``items`` | list | Stores nutrition dictionaries |
| ``history`` | DataFrame | Stores past searches |
| ``result`` | dict | API response for a food |
| ``totals`` | dict | Summed nutrition values |

## Structure Chart (Mermaid)

```mermaid
flowchart TD

    A[main()] --> B[show_help()]
    A --> C[display_nutrition(result)]
    A --> D[get_nutrition(food)]
    A --> E[calculate_totals(items)]
    A --> F[graph_single_food(item)]
    A --> G[graph_multiple_foods(items)]

    D --> D1[Sends API request]
    D --> D2[Handles errors and timeouts]
    D --> D3[Returns nutrition dictionary or None]

    E --> E1[Adds nutrition values for multiple foods]

    F --> F1[Creates bar chart for one food]

    G --> G1[Creates stacked bar chart for multiple foods]
```
## Flowcharts and Algorithms
### main()
#### Flowchart:

    A[Start Program] --> B[Display Welcome Message]
    B --> C[User Enters Input]

    C --> D{Input Type?}

    D --> E[help] --> F[show_help()] --> C
    D --> G[history] --> H[Display History] --> C
    D --> I[exit] --> J[End Program]

    D --> K[Food Input]
    K --> L[Split Foods]
    L --> M[Loop Through Foods]
    M --> N[get_nutrition()]
    N --> O{Valid?}
    O --> P[Display Nutrition] --> Q[Add to History]
    O --> R[Show Error]

    Q --> S{Multiple Foods?}
    S --> T[calculate_totals()] --> U[Display Totals]
    S --> V[Skip Totals]

    U --> W[Ask for Graph]
    V --> W

    W --> X{Graph?}
    X --> Y[graph_single_food or graph_multiple_foods]
    X --> C

    Y --> C

#### Algorithm

    BEGIN
     PRINT welcome message
     LOOP forever:
        INPUT user_input

      IF user_input == "exit":
          END PROGRAM

      IF user_input == "help":
          CALL show_help()
          CONTINUE LOOP

      IF user_input == "history":
          DISPLAY history
          CONTINUE LOOP

      IF user_input is empty:
          PRINT error
          CONTINUE LOOP

      foods = split user_input by comma
      items = empty list

      FOR each food in foods:
          result = get_nutrition(food)
          IF result exists:
              display_nutrition(result)
              add result to items
              add to history
          ELSE:
              PRINT error

      IF more than one item:
          totals = calculate_totals(items)
          DISPLAY totals

      ASK user if they want a graph
      IF yes:
          IF one item:
              graph_single_food(item)
          ELSE:
              graph_multiple_foods(items)
    END

