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
# print(soup.find('p').getText())
# print(soup.find('p').getText())
# print(soup.get_text())

whitelist = [
    'p'
]
blackList = [
    '\n', ' ', 'E-posta', ' ', 'Telefon', 'Mesaj', 'İsim'
]


def getWod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    liste = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]
    # liste = [t + ',' for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]

    # smallerlist = [l.split('|') for l in '|'.join(liste).split(',')]

    return liste
    # for wod in wods:
    #    print(wod, sep='/n')


# print(text_elements,sep='/n' )

url = 'https://crossfit34.com/gunun-antrenmani/page/'

listem = []
aralik = range(1, 3)  # includes 1, but not 3
for i in aralik:
    url = url + str(i)  # + "/"
    listem.append(getWod(url))

    time.sleep(1)

# print(listem)
# print(len(listem))
# wodsCombinedComa = ','.join(listem[0])

wodsCombinedComa = ""
i = 0
while i < len(listem):
    wodsCombinedComa += ','.join(listem[i])
    i += 1

print(wodsCombinedComa)
print(wodsCombinedComa.split(','))
print(len(wodsCombinedComa.split(',')))

# for x in listem:
#     print(x)

# f = open('antremanlar.txt', 'w+')
#
# for x in listem:
#     f.write(x)
#
# f.close()
