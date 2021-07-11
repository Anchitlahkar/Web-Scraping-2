import pandas as pd
import os
import time
import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
print('fetching data...')

time.sleep(5)

temp_star_data = []
star_data = []

headers = ["name", "distance", "mass", "radius"]

Soup = BeautifulSoup(page.content, "html.parser")

temp_list = []
print('finding data....')
for tr_tags in Soup.find_all('tr'):

    td = tr_tags.find_all("td")
    rows = [i.text.rstrip() for i in td]
    temp_list.append(rows)

print('removing unwanted data...')

temp_list.remove(temp_list[0])
temp_list.remove(temp_list[1])
temp_list.remove(temp_list[2])

name = []
distance = []
mass = []
radius = []

removeList = list(temp_list)


for i in range(1, len(temp_list)):
    try:
        name.append(temp_list[i][0])
        distance.append(temp_list[i][5])
        mass.append(temp_list[i][8])
        radius.append(temp_list[i][9])

    except:
        name.append(' ')
        distance.append(' ')
        mass.append(' ')
        radius.append(' ')

os.system("CLS")

print('creating csv....')
rows = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=[
                    'Star_name', 'Distance', 'Mass', 'Radius'])

rows.to_csv('star_data.csv')

print('All Done...')