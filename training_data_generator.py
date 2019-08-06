import requests
from bs4 import BeautifulSoup
import pandas as pd

SHOPPING_URL = 'https://www.google.com/search?q=smartphones&source=lnms&tbm=shop'

req = requests.get(SHOPPING_URL)
soup = BeautifulSoup(req.text, "lxml")

j1 = soup.find_all('div', {'class': 'g'})
j2 = [j.find_all('div', {'class': 'pslires'}) for j in j1]

data = {'Name': [], 'Price': [], 'Retailer': [], 'Stars': [], 'Description': []}

for i in range(len(j2)):
    try:
        name = j2[i][0].find_all('a')[1].text
        data['Name'].append(name)
    except:
        data['Name'].append('none')

    try:
        price = j2[i][0].find_all('div')[2].text.replace('\xa0', ' ')
        reta = j2[i][0].find_all('div')[3].text.replace('\xa0', ' ')
        data['Price'].append(price)
        data['Retailer'].append(reta)
    except:
        data['Price'].append('none')
        data['Retailer'].append('none')

    try:
        desc = j2[i][0].find_all('div')[5].text
        data['Description'].append(desc)
    except:
        data['Description'].append('none')

    try:
        stars = str(j2[i][0].find_all('div')[6]).split('"')[1].replace('\xa0', ' ')
        if 'Stern' in stars:
            stars = stars.split(' von')
            stars = stars[0]
            data['Stars'].append(stars)
        else:
            data['Stars'].append('none')
    except:
        data['Stars'].append('none')

df = pd.DataFrame(data=data)
df.to_excel("output.xlsx")
