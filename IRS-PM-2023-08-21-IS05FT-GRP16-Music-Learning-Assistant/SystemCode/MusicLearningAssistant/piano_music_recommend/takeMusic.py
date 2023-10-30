import os
from bs4 import BeautifulSoup
import csv
import requests

def main(down_load_dir=(os.path.expanduser('~') + "/Desktop/eop/")):
     headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
     }
     print("Download directory:" + down_load_dir)

     #Send a request to get the total number of piano songs
     init_music_no = "0000000"
     url = "https://www.everyonepiano.cn/Music"
     response = requests.get(url, headers=headers)
     response.encoding = "utf-8"
     soup = BeautifulSoup(response.text, features="html.parser")

     # Get the total number of music
     count = int(soup.find_all(name="div", attrs={"class": "EOPPageNo"})[0].find_all(name="span")[0].text)
     last_error_page_count = 0
     i = 12285

     # count
     with open(file='pianoMusic.csv', encoding="utf-8", mode="a") as f:
         writer = csv.writer(f, lineterminator='\n')
         writer.writerow(["title", "author", "musicType"])
         while i < count or last_error_page_count < 10:
             music_no = str(i)
             print("Getting resources" + music_no + "information...")

             url = "https://www.everyonepiano.cn/Music-" + music_no + "-"
             response = requests.get(url, headers=headers)
             response.encoding = "utf-8"

             soup = BeautifulSoup(response.text, features="html.parser")
             breadcrumbs = soup.find_all(name="ol", attrs={"class": "breadcrumb"})
             if len(breadcrumbs) > 0:
                 last_error_page_count = 0
                 author_element = soup.find_all(name="div", attrs={"class": "EOPReadInfoTxt"})[0].find_all("li")[0]
                 if "Singer/Author" in author_element.text:
                     author = author_element.find_all("a")[0].text

                 else:
                     author = ""
                 breadcrumbs = breadcrumbs[0].find_all("li")

                 title = breadcrumbs[-1].text.replace("/", " ")
                 author = author.replace("/", " ")
                 # author = author_element.find_all("a")[0].text
                 musicType = breadcrumbs[-2].text.replace("/", " ")
                 writer.writerow((title, author, musicType))

             else:
                 print("resource" + str(i) + "does not exist")
                 count += 1
                 last_error_page_count += 1
             i += 1

         f.close()


if __name__ == "__main__":
      try:
          main()

      except IndexError:
          main()