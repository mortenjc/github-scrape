from github import Github
from pprint import pprint
import pandas as pd
import json, argparse

def addtag(tag, text):
    return '<' + tag + '>' + text + '</' + tag + '>\n'

def maketable(headers, entries):
    table = '<table id="repos">'
    table = table + '<tr>'
    for header in headers:
        table = table + addtag('th', header)
    table = table + '</tr>'
    return table


def get_repo_dict(repo):
    return {"name": repo.full_name,
            "description": repo.description,
            "created": repo.created_at,
            "pushdate": repo.pushed_at,
            "homrpage": repo.homepage,
            "language": repo.language,
            "nforks": repo.forks,
            "nstars": repo.stargazers_count,
            "topics": repo.get_topics(),
            "labels": [i._rawData for i in repo.get_labels()],
            "contributors": [i._rawData for i in repo.get_contributors()],
            "ncontributors": repo.get_contributors().totalCount,
            "nsubscribers": repo.get_subscribers().totalCount,
            "nwatchers": repo.get_watchers().totalCount,
            "nissues" : repo.get_issues().totalCount,
            "nbranches" :repo.get_branches().totalCount
           }

def report(g, reponame):
    fullreponame = "ess-dmsc/" + reponame
    repo = g.get_repo(fullreponame)
    dict = get_repo_dict(repo)

    print("{:25} {:5} {:5} {:13} {:11} {:4} {:4}".format(
        reponame, dict["nforks"], dict["nstars"],\
        dict["ncontributors"], dict["nsubscribers"],
        dict["nissues"], dict["nbranches"]))


def getrepos(g, user):
    user = g.get_user(user)
    repos = user.get_repos()

    non_forks = []
    for repo in user.get_repos():
        if repo.fork is False:
            non_forks.append(repo.name)

    return non_forks


def scrape(token):
    repos = ["event-formation-unit" , "h5cpp", "daquiri", "daqlite", "efu-legacy-modules"]
    g = Github(token)

    #repos = getrepos(g, 'ess-dmsc')

    print("{:27} {:4} {:4} {:4} {:4} {:4} {:4}".format(
        "repository", "forks", "stars", "contributors", "subscribers", "issues", "branches"))

    for reponame in repos:
        report(g, reponame)


#
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", metavar="token", help="github token", type=str, default="")
    args = parser.parse_args()


    #headers = ['a', 'b', 'c']
    #print(maketable(headers, headers))

    scrape(args.t)
