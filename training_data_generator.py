import requests
from bs4 import BeautifulSoup
import pandas as pd

SHOPPING_URL = 'https://www.google.com/search?q=smartphones&source=lnms&tbm=shop&start='
OUTPUT_FILE = 'data.xlsx'


def get_items(page=0):
    req = requests.get(SHOPPING_URL + str(page * 20))
    soup = BeautifulSoup(req.text, "html.parser")
    item_containers = soup.find_all('div', {'class': 'g'})
    items = [j.find_all('div', {'class': 'pslires'}) for j in item_containers]
    return items


def parse_items(data: dict, items: list):
    for i in range(len(items)):
        try:
            item = items[i][0]
        except:
            return
        try:
            name = item.find_all('a')[1].text
            data['Name'].append(name)
        except:
            data['Name'].append('none')
        try:
            price = item.find_all('div')[2].text.replace('\xa0', ' ')
            reta = item.find_all('div')[3].text.replace('\xa0', ' ')
            data['Price'].append(price)
            data['Retailer'].append(reta)
        except:
            data['Price'].append('none')
            data['Retailer'].append('none')

        try:
            desc = item.find_all('div')[5].text
            data['Description'].append(desc)
        except:
            data['Description'].append('none')

        try:
            stars = str(item.find_all('div')[6]).split('"')[1].replace('\xa0', ' ')
            if 'Stern' in stars:
                stars = stars.split(' von')
                stars = stars[0]
                data['Stars'].append(stars)
            else:
                data['Stars'].append('none')
        except:
            data['Stars'].append('none')


if __name__ == "__main__":
    i = 0
    data = {'Name': [], 'Price': [], 'Retailer': [], 'Stars': [], 'Description': []}
    while True:
        items = get_items(page=i)
        i = i + 1
        if len(items) == 0:
            break
        else:
            parse_items(data, items)
            print("Page %i" % (i))

    df = pd.DataFrame(data=data)
    df.to_excel(OUTPUT_FILE)
