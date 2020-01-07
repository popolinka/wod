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
for i in range(1, 7):
    url = 'https://crossfit34.com/gunun-antrenmani/page/{}'.format(i) + '/'
    wods.append(getwod(url))
    time.sleep(10) # to abide /robots.txt

wodsCombinedComa = ""
i = 0
while i < len(wods):
    wodsCombinedComa += '?'.join(
        wods[i])  # any character that is not present within the wods will work. if not, it will split the wods themselves
    wodsCombinedComa += "?"
    i += 1

wodsCombinedComaSplit = wodsCombinedComa.split('?')

corrections = [("ı", "i"), ("Burpees", "Burpee"), ("Dumbbel", "Dumbbell"), ("dumbbells", "Dumbbell"),
                ("&", " & "), ("+ ", " + "), ("+", " + "), ("   +  ", " + "), (" )", ")"), ("(", " ("), (" (", " ("),
                ("Paralel", "Parallel"), ("Russain", "Russian")]

for a, b in corrections:
    wodsCombinedComaSplit = [s.replace(a, b) for s in wodsCombinedComaSplit]

f = open('CS34_wods.txt', 'w+')

for x in wodsCombinedComaSplit:
    f.write('%s\n' % x)  # splitting each wod/item into a separate row

    # TODO wodsCombinedComaSplit.append(x[:-1]) # removing the last /n line

f.close()
