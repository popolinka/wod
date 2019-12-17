import requests
import time
from bs4 import BeautifulSoup


def getwod(url):
    listem = []
    # url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    wods = soup.findAll("div", {"class": "post-body entry-content"})

    if wods:  # TODO: derdin ne abi, aslinda wods != [] in simple hali o
        for wod in wods:
            if len(wod) > 0:
                listem.append(wod.text.replace('\n', ''))
            else:
                pass
    if wods:
        return [wods, listem]


# print(len(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")))
# print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01"))

print(len(getwod("http://crossfitbalabanlevent.blogspot.com/2014/10")))
print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/10")[1])

# print(len(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")))
print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01") == None)
#print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")[1] != [])
#print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")[1])



link = "http://crossfitbalabanlevent.blogspot.com/"

workouts = []
years = [2014, 2015]
months = ["09", "10", "11", "12"]
# updated Python does not support format 01 02 etc.
# TODO: when the if statement is triggered, the output is simply an emtpy list

for y in years:
    for m in months:
        link = link + str(y) + "/" + m + "/"
        if getwod(link) is None:
            pass
        else:
            workouts.append(getwod(link)[1])

    time.sleep(1)

# print(getwod("http://crossfitbalabanlevent.blogspot.com/2019/10/"))

print(workouts)
