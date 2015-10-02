import re
import asyncio
import requests
from simpleyapsy import IPlugin


class GithubParser(IPlugin):
    def __init__(self):
        super().__init__()
        self.name = 'github-parser'
        # TODO add in a few more matches
        self.matches = [re.compile('github')]

    def __call__(self, user, repo):
        url = 'https:api.github.com/repos/{user}/{repo}'.format(user,
                                                                repo)

        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, requests.get, url)
        data = yield from future
        data = data.json()
        return data['stargazers_count'], data['forks_count']
