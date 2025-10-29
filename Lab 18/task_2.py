import requests
import json

def display_weather(city):
    api_key = "60955c8f131f9dc48b5acbc7ef62b022"  # ✅ Your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request with a timeout
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

        # Convert response to JSON
        weather_data = response.json()

        # Check if API returned an error message
        if weather_data.get("cod") != 200:
            print("Error:", weather_data.get("message", "Unknown error"))
        else:
            # Print formatted JSON data
            print(json.dumps(weather_data, indent=4))

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
    except requests.exceptions.HTTPError as e:
        print("Error: Invalid response from API.", e)
    except Exception as e:
        print("Error: Could not connect to API. Check your API key or network connection.")
        print("Details:", e)

# Example usage
city_name = input("Enter city name: ")
display_weather(city_name)
