from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import tqdm

def scrape_abe_infoservice(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="lxml")
    website_list = [x.get_text() for x in soup.find_all('td', {'class': "views-field views-field-title"})]
    new_website_list = []
    for item in website_list:
        new_website_list.append(item.strip())
    return new_website_list

full_website_list = []
for i in tqdm.tqdm(range(0, 16)):
    url = (f'https://www.abe-infoservice.fr/liste-noire/listes-noires-et-alertes-des-autorites?title=&field_denomination_value=&field_date_added_value_op=%3C&field_date_added_value%5Bvalue%5D%5Bdate%5D=20/04/2021&field_date_added_value%5Bmin%5D%5Bdate%5D=20/04/2021&field_date_added_value%5Bmax%5D%5Bdate%5D=&items_per_page=200&page={i}')
    temp_list = scrape_abe_infoservice(url)
    for item in temp_list:
        full_website_list.append(item)

print(len(full_website_list))

with(open('/home/anastasia/Documents/draft_projects/Validalab_scraping/batch9_validalab/scrape_and_push_abe_infoservices/abe_infoservice.json', 'w', encoding = 'utf8')) as f:
    json.dump(full_website_list, f, ensure_ascii=False)
