from bs4 import BeautifulSoup
import requests
resp = requests.get("https://www.flipkart.com")
soup = BeautifulSoup(resp.text)
for item in soup.find_all("img"):
    print(item['href'])