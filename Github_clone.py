import os

import requests

# To clone the data directly from github to current working directory
response = requests.get('https://api.github.com/repos/PhonePe/pulse')
repo = response.json()
clone_url = repo['clone_url']
repo_name = "pulse"
clone_dir = os.path.join(os.getcwd(), repo_name)
