import json
from datetime import datetime

# Load the repository data from the JSON file
with open("github_repos.json", "r") as f:
    repos = json.load(f)

# Open the Markdown file for writing
with open("github_repos.md", "w", encoding="utf-8") as f:
    # Write the Markdown header
    f.write("# Awesome GitHub Repositories with 1000+ Stars 🌟\n\n")
    f.write("This is a list of GitHub repositories that have more than 1000 stars, including their description, number of stars, title, author, and created date.\n\n")

    # Loop through the repositories and write the Markdown content
    for repo in repos:
        f.write(f"## [{repo['name']}]({repo['html_url']}) 🔗\n\n")
        f.write(f"**Description:** {repo['description']}\n\n")
        f.write(f"**Stars:** {repo['stargazers_count']} ⭐\n")
        f.write(f"**Title:** {repo['full_name']}\n")
        f.write(f"**Author:** {repo['owner']['login']} 👤\n")
        created_at = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        f.write(f"**Created:** {created_at.strftime('%B %d, %Y')} 📅\n\n")
        f.write("---\n\n")

print("Markdown file 'github_repos.md' created successfully!")