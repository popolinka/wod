import requests
import time
import re
from bs4 import BeautifulSoup

# TODO: More than 2 MONTHS/YEARS does not crawl


def getwod(url):
    listem = []
    # url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    wods = soup.findAll("div", {"class": "post-body entry-content"})

    if wods:
        for wod in wods:
            if len(wod) > 0:
                listem.append(
                    re.sub("\s+", " ", wod.text.replace('\n', ' ').strip()))
                # trailing whitespaces AND large spaces in between words are removed here
            else:
                pass
    if wods:
        return [wods, listem]


link = "http://crossfitbalabanlevent.blogspot.com/"

workouts = []
years = [2014, 2015]
# year 2014 only has 3 months, compromise, too much effort, let it go.
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
# updated Python does not support format 01 02 etc.

for y in years:
    link = link + str(y) + "/"
    for m in months:
        link = link + m + "/"
        if getwod(link) is not None:
            workouts.append(getwod(link)[1])
        # else:

    time.sleep(1)

with open('BalabanCS_wods.txt', 'w') as f:  # with => no need to f.close()
    f.writelines('\n'.join(workouts[0]))

# Check that the file has been automatically closed.
print(f.closed)

"""
as per https://docs.python.org/3/tutorial/inputoutput.html
It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times.

After a file object is closed, either by a with statement or by calling f.close(), attempts to use the file object will automatically fail.
"""
