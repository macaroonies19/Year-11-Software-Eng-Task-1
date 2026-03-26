# Nutrition API
A command line application that retrieves nutrition data for foods using an open‑source API, displays results, calculates totals for multiple foods, and optionally generates graphs.

## How to Run the Application
1. Clone or download the repository
- git clone <https://github.com/macaroonies19/Year-11-Software-Eng-Task-1>
2. Install dependencies
- In the terminal, run: pip install -r requirements.txt
3. API Key
- Use my API key already provided or get your own from API Ninjas.
4. Run the program
- Start the app with: python main.py

## How to Use the Program
After entering foods, the program will:
- Fetch nutrition data from the API
- Display results immediately
- Calculate totals if multiple foods were entered
- Ask if you want to generate a graph

## Dependencies
All dependencies are listed in requirements.txt, but the key modules are:
- requests
- pandas
- matplotlib