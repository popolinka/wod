import requests
import time
from bs4 import BeautifulSoup

whitelist = [
    'p', 'h4', 'div', 'h3'
]
blackList = [
    '\n', ' ', 'E-posta', ' ', 'Telefon', 'Mesaj', 'İsim'
]


def getwod(url):
    listem = []
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    wods = soup.findAll("div", {"class" : "post-body entry-content"})
    for wod in wods:
        listem.append(wod.text.replace('\n', '')
)
    # wod = soup.findAll("span", {"span style": "font-size: large;"})

    # liste = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]
    # liste = [t for t in soup.findAll("div", {"class" : "post-body entry-content"}) if t.parent.name in whitelist and t not in blackList]

    return listem


print(getwod("http://crossfitbalabanlevent.blogspot.com/2019/10/"))
