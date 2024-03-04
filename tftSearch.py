import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
from requests_html import HTMLSession

#Get data
session = HTMLSession()
print("Accessing https://mobalytics.gg/tft/tier-list/team-comps...")
r = session.get('https://mobalytics.gg/tft/tier-list/team-comps')
r.html.render()
compText = r.html.find('.m-1bpc5zi', first = False)
statText = r.html.find('.m-1rhbarm', first = False)

#Write to file
file = open("compdata.csv", "w")
file.writelines("comp,avg. place\n")

for i in range(0,5):

    file.writelines(compText[i].text + "," + statText[i*4].text + "\n")
    

file.close()

#Display table
dataframe = pd.read_csv("compdata.csv")
print(dataframe)