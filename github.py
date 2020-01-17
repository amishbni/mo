import requests
from dateutil import parser

def version():
    repository = "https://api.github.com/repos/amirashabani/mo/commits/master"

    response = requests.get(repository).json()

    last_commit = response["commit"]["author"]["date"]

    # last_commit_parsed
    lcp = parser.parse(last_commit)

    return f"{lcp.year}.{lcp.month:02}.{lcp.day:02}"

