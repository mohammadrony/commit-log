import os
import requests
from requests.exceptions import RequestException

def main():
  repository = os.getenv("GITHUB_REPOSITORY", "dsinnovators/js-essentials")
  api_url = f"https://api.github.com/repos/{repository}/commits"
  print(f"{repository}\n---------------------------------")
  
  try:
    response = requests.get(api_url)
    
    if response.status_code == 409:
      print("No commit found.")
      return
    
    response.raise_for_status()
    commits = response.json()

    for commit in commits:
      author_name = commit['commit']['author']['name']
      message = commit['commit']['message']
      print(f"{author_name}: {message}")

  except RequestException as e:
    print(f"Network error occurred: {e}")

if __name__ == "__main__":
  main()
