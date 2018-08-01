from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
soup = BeautifulSoup(resp.text)
for item in soup.find_all("item"):
    try:
        print(item.find("pubDate").text)
    except:
        print(item.find("title").text)
