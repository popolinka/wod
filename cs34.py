import requests
import time
from bs4 import BeautifulSoup

whitelist = ['p']
blackList = ['\n', ' ', 'E-posta', ' ', 'Telefon', 'Mesaj', 'İsim']


def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    workouts = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]

    return workouts


wods = []
aralik = range(1, 7)  # includes 1, but not 3
for i in aralik:
    url = 'https://crossfit34.com/gunun-antrenmani/page/{}'.format(i) + '/'
    wods.append(getwod(url))
    # ilk savfayi bitirip ikinci sayfaya gecerken bosluk birakmasi lazim, yoksa son ve ilk idman birlesiyor

    time.sleep(10) # as per /robots.txt

wodsCombinedComa = ""
i = 0
while i < len(wods):
    wodsCombinedComa += '?'.join(
        wods[i])  # text lerde olmayan bir karakter olmasi onemli, yoksa text in kendisni 2 ayri parcaya boluyor
    wodsCombinedComa += "?"
    i += 1

wodsCombinedComaSplit = wodsCombinedComa.split('?')

degisecekler = [("ı", "i"), ("Burpees", "Burpee"), ("Dumbbel", "Dumbbell"), ("dumbbells", "Dumbbell"),
                ("&", " & "), ("+ ", " + "), ("+", " + "), ("   +  ", " + "), (" )", ")"), ("(", " ("), (" (", " ("),
                ("Paralel", "Parallel"), ("Russain", "Russian")]

for a, b in degisecekler:
    wodsCombinedComaSplit = [s.replace(a, b) for s in wodsCombinedComaSplit]

print(len(wodsCombinedComaSplit))

f = open('CS34_wods.txt', 'w+')

for x in wodsCombinedComaSplit:
    f.write('%s\n' % x)  # splitting each wod/item into a separate row

    # TODO wodsCombinedComaSplit.append(x[:-1]) # removing the last /n line

f.close()
