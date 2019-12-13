import requests
import time
from bs4 import BeautifulSoup


whitelist = [
    'p' , 'h4', 'div' , 'h3'
]
blackList = [
    '\n', ' ', 'E-posta', ' ', 'Telefon', 'Mesaj', 'İsim'
]

def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # wod = soup.findAll("div", {"class" : "post-body entry-content"})
    wod = soup.findAll("span", {"span style": "font-size: large;"})

    # liste = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]

    return wod

print(getwod("http://crossfitbalabanlevent.blogspot.com/2019/10/"))
