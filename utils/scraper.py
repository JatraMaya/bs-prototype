from requests import get
from re import search
from bs4 import BeautifulSoup as BS

KEYWORD = r"'https://connect\.facebook\.net/en_US/fbevents.js'"

def scrapped(url):
    data = get(url).text
    soup = BS(data, 'html.parser')
    scripts = soup.find_all("script")

    for s in scripts:
        if s.string is not None:
            result = search(KEYWORD, s.string)
            if result is not None:
                data = {"url": url, "status": "Script found.", "script": s.string}
                return data
    return {"url": url, "status": "Script not found."}
# keyword = r"'https://connect\.facebook\.net/en_US/fbevents.js'"

# url = "https://www.psb-academy.edu.sg/"
# url = "https://www.ncs.co/en-sg"
# url = "https://www.ncs.com.cn/zh-cn"

# data = urlopen(url).read().decode("utf-8")
# soup = BS(data, 'html.parser')
# scripts = soup.find_all("script")

# def main():
#     for s in scripts:
#         if s.string is not None:
#             result = search(keyword, s.string)
#             if result:
#                 print(s.string)

# if __name__ == "__main__":
#     main()
