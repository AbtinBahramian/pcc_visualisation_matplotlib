import requests

#make the API call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

GITHUB_TOKEN = "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"

# Set up the headers
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"  # GitHub recommends specifying the API version
}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#conver to dictionary
response_dict = r.json()

print(f"total amount of repositories: {response_dict['total_count']}")
print(f"Complete Results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict.keys())}")
for key in sorted(repo_dict.keys()):
    print(key)

#more data about our first repository

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

