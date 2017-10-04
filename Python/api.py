"""
The Python module requests can translate Json responses into Python dictionaries.
http://docs.python-requests.org/en/master/user/quickstart/#response-content
"""

import requests

r = requests.get("http://api.icndb.com/jokes/random")

# print(r.json())

usable = r.json()

print(usable['value']['joke'])