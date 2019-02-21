import requests
from bs4 import BeautifulSoup

url = 'http://whatsmyuseragent.com/'
headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
ua = soup.select_one(".user-agent").get_text()

print("YOUR USER AGENT REPORT IS:")
print()
print(ua)
