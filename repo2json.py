import requests
import json
import logging

# Set up logging
logging.basicConfig(filename='github_repos.log', level=logging.INFO)

# Set the GitHub API endpoint URL
url = "https://api.github.com/search/repositories"

# Set the search parameters
params = {
    "q": "stars:>1000",
    "sort": "stars",
    "order": "desc",
    "per_page": 100  # Fetch up to 100 results per page
}

# Initialize an empty list to store the repository data
repos = []

# Fetch the repository data in pages
page = 1
while True:
    params["page"] = page
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Add the repositories to the list
        repos.extend(response.json()["items"])
        
        # Check if there are more pages to fetch
        if "next" not in response.links:
            break
        page += 1
    else:
        logging.error(f"Error fetching data: {response.status_code}")
        break

# Save the repository data to a file
with open("github_repos.json", "w") as f:
    json.dump(repos, f, indent=4)

logging.info(f"Saved {len(repos)} GitHub repositories with more than 1000 stars to 'github_repos.json'.")