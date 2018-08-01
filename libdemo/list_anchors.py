from bs4 import BeautifulSoup
import requests
resp = requests.get("http://www.srikanthtechnologies.com")
soup = BeautifulSoup(resp.text)
for item in soup.find_all("a"):
    print(item['href'])