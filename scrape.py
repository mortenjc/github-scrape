from github import Github
from pprint import pprint
import pandas as pd
import json

def get_repo_dict(repo):
    return {"Full name": repo.full_name,
            "Description": repo.description,
            "Date created": repo.created_at,
            "Date of last push": repo.pushed_at,
            "Home Page": repo.homepage,
            "Language": repo.language,
            "Number of forks": repo.forks,
            "Number of stars": repo.stargazers_count,
            "Topics": repo.get_topics(),
            "Labels": [i._rawData for i in repo.get_labels()],
            "Contributors": [i._rawData for i in repo.get_contributors()],
            "Contributors Count": repo.get_contributors().totalCount,
            #"Subscribers": [i._rawData for i in repo.get_subscribers()],
            "Subscribers Count": repo.get_subscribers().totalCount,
            #"Watchers": [i._rawData for i in repo.get_watchers()],
            "Watchers Count": repo.get_watchers().totalCount
           }

repos = ["event-formation-unit", "h5cpp", "forwarder", "daqlite", "efu-legacy-modules"]

g = Github("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")

def report(reponame):
    fullreponame = "ess-dmsc/" + reponame
    repo = g.get_repo(fullreponame)
    dict = get_repo_dict(repo)
    issues = repo.get_issues()

    print("{:25} {:5} {:5} {:13} {:11} {:4}".format(
        reponame, dict["Number of forks"], dict["Number of stars"],\
        dict["Contributors Count"], dict["Subscribers Count"], issues.totalCount))

print("{:25} {:4} {:4} {:4} {:4} {:4}".format(
    "Repository", "forks", "stars", "contributors", "subscribers", "issues"))

for reponame in repos:
    report(reponame)


# # g = Github("<Github user key>") # insert key for a higher rate limit
# TOPIC = "interview-practice"
#
# # search by topic
# all_repo = g.search_repositories(f'topic:{TOPIC}')
# print(all_repo.totalCount) # returns 678 repositories
