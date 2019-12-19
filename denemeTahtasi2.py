import requests
import time
import re
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
                listem.append(wod.text.replace('\n', ' '))
                # listem.append(wod.text)
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
print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01"))

# print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")[1] != [])
# print(getwod("http://crossfitbalabanlevent.blogspot.com/2014/01")[1])


link = "http://crossfitbalabanlevent.blogspot.com/"

workouts = []
years = [2015, 2016]
# year 2014 only has 3 months, compromise, too much effort, let it go.
months = ["01", "02"]
# updated Python does not support format 01 02 etc.
# TODO: when the if statement is triggered, the output is simply an emtpy list

for y in years:
    link = link + str(y) + "/"
    for m in months:
        link = link + m + "/"
        if getwod(link) is not None:
            workouts.append(getwod(link)[1])
        # else:

    time.sleep(1)

# print(getwod("http://crossfitbalabanlevent.blogspot.com/2019/10/"))

# some regex
for workout in workouts[0]:
    workout = workout.strip()
    # workout = re.sub("\s+", " ", workout)
    workout = re.sub(' {2,}', ' ', workout)

f = open('BalabanCS_wods.txt', 'w+')

for x in workouts[0]:
    f.write('%s\n' % x)  # splitting each wod/item into a seperate row

    # TODO wodsCombinedComaSplit.append(x[:-1]) # removing the last /n line

f.close()

# print(workouts)
# print(type(workouts))
# print(len(workouts))
# print(len(workouts[0]))
