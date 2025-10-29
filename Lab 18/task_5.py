import requests
import json

def display_weather(city):
    api_key = "60955c8f131f9dc48b5acbc7ef62b022"  # ✅ Your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()  # Raise error for 4xx/5xx responses

        # Convert response to JSON
        data = response.json()

        # Display formatted JSON
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)

        # Append JSON data to a text file
        with open("weather_data.txt", "a", encoding="utf-8") as file:
            file.write(f"\nCity: {city}\n")
            file.write(formatted_json)
            file.write("\n" + "-"*50 + "\n")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid API request. Please check your API key or city name.")
    except Exception as e:
        print("Error:", str(e))


# ---- Run the function ----
city_name = input("Enter city name: ")
display_weather(city_name)
