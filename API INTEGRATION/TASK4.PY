
import os
import time
import requests

API_URL = "https://newsapi.org/v2/top-headlines"

CATEGORIES = {
    "sports": "sports",
    "technology": "technology",
    "health": "health"
}


def get_headlines(category):
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("Error: News API key is missing.")
        print("Set the NEWS_API_KEY environment variable and try again.")
        return

    if category not in CATEGORIES:
        print("Error: Invalid category.")
        print("Choose sports, technology, or health.")
        return

    params = {
        "category": CATEGORIES[category],
        "country": "us",
        "pageSize": 5,
        "apiKey": api_key
    }

    for attempt in range(2):
        try:
            response = requests.get(
                API_URL,
                params=params,
                timeout=10
            )

            if response.status_code == 401:
                print("Error: Invalid News API key.")
                return

            if response.status_code == 429:
                print("Error: News API request limit exceeded.")
                return

            response.raise_for_status()
            data = response.json()

            if data.get("status") != "ok":
                print("Error:", data.get("message", "Unexpected API response"))
                return

            articles = data.get("articles", [])

            if not articles:
                print("No headlines available for this category.")
                return

            print(f"\n--- Top 5 {category.title()} Headlines ---")

            for index, article in enumerate(articles[:5], start=1):
                title = article.get("title") or "Title unavailable"
                source = article.get("source", {}).get("name", "Unknown")
                url = article.get("url", "")

                print(f"\n{index}. {title}")
                print(f"   Source: {source}")
                print(f"   Link: {url}")

            return

        except requests.exceptions.Timeout:
            print(f"Request timed out (attempt {attempt + 1}/2).")
        except requests.exceptions.ConnectionError:
            print(f"Connection failed (attempt {attempt + 1}/2).")
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error}")
            return
        except (requests.exceptions.RequestException, ValueError) as error:
            print(f"Error retrieving news: {error}")
            return

        if attempt == 0:
            print("Retrying in 2 seconds...")
            time.sleep(2)

    print("Error: Unable to retrieve news after 2 attempts.")


if __name__ == "__main__":
    category = input(
        "Enter category (sports/technology/health): "
    ).strip().lower()

    get_headlines(category)
