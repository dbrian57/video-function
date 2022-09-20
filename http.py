import requests

r = requests.get('https://xkcd.com/1906/')

print(r.status_code)