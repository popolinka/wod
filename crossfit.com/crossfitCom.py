import requests
import time
import re
from bs4 import BeautifulSoup

workouts = []
link = "https://www.crossfit.com/workout/?page={}/"

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    workoutsTags = soup.findAll("div", {"class": "col-sm-6"})  # <class 'bs4.element.ResultSet'>

    for workout in workoutsTags:
        if workout.get_text() and not (workout.get_text()).startswith("Rest Day"):  # empty and "Rest Day..." check
            if not workout.get_text().split()[0] in days:  # getting rid of day + wod duplicate issue
                # y = workout.replace(old=" Post time to comments.", new="")
                y = " ".join(workout.get_text().split("\n")).strip()
                y.replace(" Post time to comments." and " Post rounds completed to comments.", "")  # TODO
                y = re.sub("\|.+", "", y)  # getting rid of | Compare to 112...
                workouts.append(y.strip())
                # TODO: Catch "Post time to comments." and erase them. also get rid of COMPARE s
                # Catching post is not always convenient, e.g. Do it on a track, upload video to YouTube, and post a lin
    return workouts


for i in range(1, 2):  # 5 exclusive
    workouts.append(getwod(link.format(i)).pop(-1))  # pop bc. since return workouts (see getwod()) adds ...
    time.sleep(5)

with open('crossfitCom_wods.txt', 'w+') as f:
    for x in workouts:
        f.write('%s\n' % x)  # splitting each wod/item into a separate row

print(workouts.pop(-1))
