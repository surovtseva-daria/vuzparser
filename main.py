import requests
from bs4 import BeautifulSoup
import csv

site_root='https://vuzopedia.ru'
f = open('vuz.csv', 'w')
# create the csv writer
writer = csv.writer(f)

def getvuz(link,name):
    page = requests.get( site_root + link)
    if page.ok:
        soup = BeautifulSoup(page.text, "html.parser")
        city=soup.select('#newChoose > span')[0].text.strip()
        # univers = soup.findAll('h1', class_='mainTitle')
        # univerpage=univers[0].next.strip()
        get_bakalavriat(link,city,name)
        #


def get_vuz_list_page(num):
    page = requests.get('https://vuzopedia.ru/vuz?page=' + str(num))
    if page .ok:
        soup = BeautifulSoup(page.text, "html.parser")
        univers = soup.findAll('div', class_='itemVuz')
        for univer in univers:
           name=univer.div.div.a.div.text.strip()
           link=univer.div.div.a['href']
           getvuz(link, name)

def get_bakalavriat(link, city, name):
    page = requests.get(site_root + link + '/bakalavriat')
    if page.ok:
        soup = BeautifulSoup(page.text, "html.parser")
        specs = soup.findAll('div', class_='itemSpecAllinfo')
        for spec in specs:
            spec_name=spec.div.a.text
            predmet=spec.select('div.egeInVuzProg')[0].span.text
            # print(city+';'+name+';'+spec_name+';'+predmet)
            # write a row to the csv file
            writer.writerow([city, name, spec_name, predmet])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for i in range(1,5000):
    #     getvuz(i)
    for i in range(1, 50):
        get_vuz_list_page(i)

    # close the file
    f.close()