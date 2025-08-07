def analyze_temperature(temp_celsius):
    """
    Analyzes the given temperature in Celsius and prints clear instructions about the temperature outside.
    """
    if temp_celsius < 0:
        print("It's freezing outside! Wear heavy winter clothing and be cautious of ice.")
    elif 0 <= temp_celsius < 10:
        print("It's very cold outside. Wear a warm coat, hat, and gloves.")
    elif 10 <= temp_celsius < 20:
        print("It's a bit chilly. A light jacket or sweater is recommended.")
    elif 20 <= temp_celsius < 30:
        print("The weather is pleasant. Comfortable clothing is suitable.")
    elif 30 <= temp_celsius < 40:
        print("It's quite hot outside. Wear light clothing and stay hydrated.")
    else:
        print("Extreme heat! Avoid going out if possible, wear very light clothes, and drink plenty of water.")

if __name__ == "__main__":
    try:
        temp = float(input("Enter the current temperature in Celsius: "))
        analyze_temperature(temp)
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
