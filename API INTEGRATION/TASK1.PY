
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm"
}


def get_weather(city):
    try:
        location_response = requests.get(
            GEOCODING_URL,
            params={"name": city, "count": 1, "language": "en"},
            timeout=10
        )
        location_response.raise_for_status()
        location_data = location_response.json()

        locations = location_data.get("results")
        if not locations:
            print("Error: City not found. Please enter a valid city.")
            return

        location = locations[0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "weather_code"
                ),
                "timezone": "auto"
            },
            timeout=10
        )
        weather_response.raise_for_status()

        current = weather_response.json()["current"]
        code = current["weather_code"]

        print("\n--- Current Weather ---")
        print(f"City: {location['name']}")
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Humidity: {current['relative_humidity_2m']}%")
        print(f"Description: {WEATHER_CODES.get(code, 'Unknown weather')}")
        print(f"Time: {current['time']}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except (requests.exceptions.RequestException, ValueError, KeyError) as error:
        print(f"Error retrieving weather data: {error}")


if __name__ == "__main__":
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Error: City name cannot be empty.")
