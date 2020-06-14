"""
Base URL: httpbin.org
this site has all the request response methods
"""
import requests

r = requests.get('https://www.python.org')
# we get the html text page as the response with .text
print(r.text)

# We get the status of response as 200
print(r)


r1 = requests.get('https://www.python.org/static/opengraph-icon-200x200.png')
# prints bytes of an image with r1.content
print(r1.content)

with open('images.png', 'wb') as f:
    f.write(r1.content)

# We get the status of response as 200
print(r1.status_code)
print(r1.headers)

payload = {'page': 2, 'count': 25}
r2 = requests.get('https://httpbin.org/get', params=payload)
print(r2.url)
print(r2.text)
print(r2.json())

r3 = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r3)