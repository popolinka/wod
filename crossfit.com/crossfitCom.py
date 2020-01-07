import requests
import time
from bs4 import BeautifulSoup

workouts = []
link = "https://www.crossfit.com/workout/"

def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    workoutsTags = soup.findAll("div", {"class": "col-sm-6"})  # <class 'bs4.element.ResultSet'>

    for workout in workoutsTags:
        if workout.get_text():  # emtpy text check
            workouts.append(" ".join(workout.get_text().split("\n")).strip())
            # TODO: For Tuesday 200107, it crawls an extra Post thoughts... check Elements of the link out
    return workouts

wods = getwod(link)

with open('crossfitCom_wods.txt', 'w+') as f:
    for x in wods:
        f.write('%s\n' % x)  # splitting each wod/item into a separate row
