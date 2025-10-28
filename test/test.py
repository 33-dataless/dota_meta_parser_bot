## для тестов любой хуйни

import requests

req = requests.get('https://dota2protracker.com/__data.json?x-sveltekit-trailing-slash=1&x-sveltekit-invalidated=11')
print(req.text)

