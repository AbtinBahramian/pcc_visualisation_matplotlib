import requests
import plotly.express as px

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
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict.keys())}")
# for key in sorted(repo_dict.keys()):
#     print(key)

repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # we added a link for each one
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    #making hover text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#make visualization
title = 'Most stared Python projcts on Github'
label = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=label, hover_name=hover_texts)

fig.update_layout(title_font_size = 28, xaxis_title_font_size= 20, yaxis_title_font_size= 20)
fig.show()
