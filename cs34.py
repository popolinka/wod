import requests
# import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://crossfit34.com/gunun-antrenmani/page/1/'
response = requests.get(url)

print(type(response))

soup = BeautifulSoup(response.text, "html.parser")
# soup.findAll('p')
# soup.get_text()
# print(type(soup.findAll('p')))
# print(soup.findAll('p'))
#  print(soup.find('p').getText())
# print(soup.find('p').getText())
# print(soup.get_text())

whitelist = [
    'p'
]
blackList = [
    '\n', ' ', 'E-posta', '\n', ' ', 'Telefon', '\n', ' ', 'Mesaj', '\n', ' ', 'İsim'
]


def getWod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return [t + ',' for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]
    # for wod in wods:
    #    print(wod, sep='/n')


# print(text_elements,sep='/n' )

url = 'https://crossfit34.com/gunun-antrenmani/page/'

listem = []
for i in range(1, 2):  # includes 0, but not 3
    url = url + str(i)  # + "/"
    listem.append(getWod(url))

    time.sleep(1)

print(listem)

# for x in listem:
#     print(x)

# f = open('antremanlar.txt', 'w+')
#
# for x in listem:
#     f.write(x)
#
# f.close()
