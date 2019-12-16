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
    # url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    wods = soup.findAll("div", {"class": "post-body entry-content"})
    for wod in wods:
        listem.append(wod.text.replace('\n', ''))

    return listem


url = "http://crossfitbalabanlevent.blogspot.com/"

workouts = []
# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
years = [2014, 2015]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
# updated Python does not support format 01 02 etc.
# TODO: when the if statement is triggered, the output is simply an emtpy list

for y in years:
    for m in months:
        url = url + str(y) + "/" + m + "/"
        # workouts.append(getwod(url))
        if getwod(url):
            workouts.append(getwod(url))

        # if requests.get(url).status_code == 200:
        #     workouts.append(getwod(url))
        # else:
        #     pass
    time.sleep(1)

# print(getwod("http://crossfitbalabanlevent.blogspot.com/2019/10/"))

print(workouts)
