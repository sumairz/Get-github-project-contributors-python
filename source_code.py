# Install certifi module to generate secure ssl3 certificate github is using that certificate 

# Requirements
# module pygithub3
# module: certifi

from pygithub3 import Github

gh = Github()

list = gh.repos.list_contributors(user="poise", repo="python")
for page in list:
    for resource in page:
        print resource
