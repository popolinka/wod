import requests
import time
from bs4 import BeautifulSoup

workouts = []
link = "https://www.crossfit.com/workout/?page={}/"

days = ["Monday", "Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" , "Saturday", "Sunday"]


def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    workoutsTags = soup.findAll("div", {"class": "col-sm-6"})  # <class 'bs4.element.ResultSet'>

    for workout in workoutsTags:
        if workout.get_text() and not (workout.get_text()).startswith("Rest Day"):  # empty and "Rest Day..." check
            if not workout.get_text().split()[0] in days: # getting rid of day + wod duplicate issue
                workouts.append(" ".join(workout.get_text().split("\n")).strip())
    return workouts


for i in range(1, 3):  # 5 exclusive
    workouts.append(getwod(link.format(i)).pop(-1))  # pop bc. since return workouts (see getwod()) adds ...
    time.sleep(5)

with open('crossfitCom_wods.txt', 'w+') as f:
    for x in workouts:
        f.write('%s\n' % x)  # splitting each wod/item into a separate row
