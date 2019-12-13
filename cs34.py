import requests
import time
from bs4 import BeautifulSoup

whitelist = [
    'p'
]
blackList = [
    '\n', ' ', 'E-posta', ' ', 'Telefon', 'Mesaj', 'İsim'
]


def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    liste = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]

    return liste


url = 'https://crossfit34.com/gunun-antrenmani/page/'

listem = []
aralik = range(1, 3)  # includes 1, but not 3
for i in aralik:
    url = url + str(i)  # + "/"
    listem.append(getwod(
        url))  # ilk savfayi bitirip ikinci sayfaya gecerken bosluk birakmasi lazim, yoksa son ve ilk idman birlesiyor

    time.sleep(1)

wodsCombinedComa = ""
i = 0
while i < len(listem):
    wodsCombinedComa += '?'.join(
        listem[i])  # text lerde olmayan bir karakter olmasi onemli, yoksa text in kendisni 2 ayri parcaya boluyor
    wodsCombinedComa += "?"
    i += 1

wodsCombinedComaSplit = wodsCombinedComa.split('?')

# print(wodsCombinedComa)
# print(wodsCombinedComaSplit)  # the last item is '', why?
print(len(wodsCombinedComaSplit))
print(type(wodsCombinedComaSplit))

degisecekler = [("ı", "i"), ("Burpees", "Burpee"), ("Dumbbel", "Dumbbell"), ("dumbbells", "Dumbbell"),
                ("&", " & "),("+ ", " + "), ("+", " + "), ("   +  ", " + "), (" )", ")"), ("(", " ("), (" (", " ("),
                ("Paralel", "Parallel")]

for a, b in degisecekler:
    wodsCombinedComaSplit = [s.replace(a, b) for s in wodsCombinedComaSplit]

f = open('antremanlar.txt', 'w+')

for x in wodsCombinedComaSplit:
    f.write('%s\n' % x)  # splitting each wod/item into a seperate row

    # TODO wodsCombinedComaSplit.append(x[:-1]) # removing the last /n line

f.close()
