import requests
from bs4 import BeautifulSoup

# Get the raw HTML with requests lib

#response = requests.get("https://google.com/")
#print(response.text)


#Using Beautiful Soup
response = requests.get("https://google.com/")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)