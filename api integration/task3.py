
import requests

GITHUB_API_URL = "https://api.github.com/repos"


def get_repository_info(owner, repo):
    url = f"{GITHUB_API_URL}/{owner}/{repo}"

    try:
        response = requests.get(
            url,
            headers={"Accept": "application/vnd.github+json"},
            timeout=10
        )

        if response.status_code == 404:
            print("Error: Repository not found. Check the owner and name.")
            return

        if response.status_code == 403:
            remaining = response.headers.get("X-RateLimit-Remaining")

            if remaining == "0":
                print("Error: GitHub API rate limit exceeded.")
            else:
                print("Error: Access denied or API rate limit reached.")
            return

        response.raise_for_status()
        data = response.json()

        print("\n--- GitHub Repository Information ---")
        print(f"Repository: {data.get('full_name', 'N/A')}")
        print(f"Description: {data.get('description') or 'No description'}")
        print(f"Stars: {data.get('stargazers_count', 0)}")
        print(f"Forks: {data.get('forks_count', 0)}")
        print(f"Open Issues: {data.get('open_issues_count', 0)}")
        print(f"URL: {data.get('html_url', 'N/A')}")

    except requests.exceptions.Timeout:
        print("Error: GitHub request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"Error retrieving repository information: {error}")


if __name__ == "__main__":
    owner = input("Enter GitHub username or organization: ").strip()
    repo = input("Enter repository name: ").strip()

    if not owner or not repo or "/" in owner or "/" in repo:
        print("Error: Enter a valid owner and repository name.")
    else:
        get_repository_info(owner, repo)
