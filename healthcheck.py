import urllib.request

response = urllib.request.urlopen('http://localhost:5000/health')

if response.status != 200:
    exit(1)

if response.read().decode('utf8') != 'OK':
    exit(1)

exit(0)
