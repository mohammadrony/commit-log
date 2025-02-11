import requests
from requests.exceptions import RequestException

def main():
  api_url = "https://api.github.com/repos/dsinnovators/js-essentials/commits"

  try:
    response = requests.get(api_url)
    response.raise_for_status()
    commits = response.json()
    
    if not commits:
      print("No commits found")
      return

    for commit in commits:
      author_name = commit['commit']['author']['name']
      message = commit['commit']['message']
      print(f"{author_name}: {message}")
          
  except RequestException as e:
    print(f"Network error occurred: {e}")

if __name__ == "__main__":
  main()
