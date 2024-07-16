import requests

# Load the HTML
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(page.text)
