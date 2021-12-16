import requests
from bs4 import BeautifulSoup


def Codeforces(url):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    upcomingDiv = soup.find_all("div")
    upcomingTable = upcomingDiv[40].find_all('tr')

    print(f"[Codeforces:{url}]")
    for i in range(1, len(upcomingTable)):
        schedule = f"            {upcomingTable[i].contents[5].text.strip()}"
        schedule += f" | {upcomingTable[i].contents[1].text.strip()}"
        print(schedule)


def Atcoder(url):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    upcomingDiv = soup.find("div", {"id": "contest-table-upcoming"})
    upcomingTable = upcomingDiv.find_all('tr')

    print(f"[Atcoder:{url}]")
    for i in range(1, len(upcomingTable)):
        schedule = f"         {upcomingTable[i].contents[1].text.strip()}"
        schedule += f" | {upcomingTable[i].contents[3].contents[3].text.strip()}"
        print(schedule)


print(f"Upcoming Contest List...")
codeforcesURL = "https://codeforces.com/contests"
Codeforces(codeforcesURL)

atcoderURL = "https://atcoder.jp/contests/"
Atcoder(atcoderURL)
