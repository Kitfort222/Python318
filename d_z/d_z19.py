# import requests
#
#
# r = requests.get("https://alisavet.ru/")
# print(r.text)
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


# def write_csv(data):
#     with open("alisa.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['pl']))


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    p1 = soup.find("div", class_="main-advantages__list")
    pl = p1.find_all("div", class_="main-advantages__list-item")

    return pl

# data = []
# write_csv(data)


def main():
    url = "https://alisavet.ru/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
