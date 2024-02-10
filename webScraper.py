import requests
from requests_html import HTMLSession

# Get the raw HTML with requests lib

#response = requests.get("https://google.com/")
#print(response.text)


#Using Beautiful Soup
'''print("Accessing https://google.com/")
response = requests.get("https://google.com/")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
print()'''

#Using selenium

#Using requestsHTML
session = HTMLSession()
r = session.get('https://www.metatft.com/comps')
r.html.render()
about = r.html.find('.Comp_Title', first = False)

for i in range(0,5):
    print(about[i].text)

