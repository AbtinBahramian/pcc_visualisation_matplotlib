from operator import itemgetter
import plotly.express as px
import requests
import json

# make an API call
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

#process information for each submission
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:10]:
     # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    #build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
        'comments' : response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

discussion_links, comments_count = [], []
for submission_dic in submission_dicts:
    comments_count.append(submission_dic['comments'])

    discussion_title = submission_dic['title']
    discussion_link = f"<a href='{submission_dic['hn_link']}'>{discussion_title}</a>"
    print(discussion_link)
    discussion_links.append(discussion_link)

label = {'x': 'Discussions', 'y': 'Comments'}
fig = px.bar(x=discussion_links, y=comments_count, labels=label, title="Hacker news articles with most comments")
fig.show()

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discusion Link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")