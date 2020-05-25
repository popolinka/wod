import scrapy
from scrapy.crawler import CrawlerProcess

def getwod(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    workouts = [t for t in soup.find_all(text=True) if t.parent.name in whitelist and t not in blackList]

    return workouts

