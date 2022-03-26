import requests
from bs4 import BeautifulSoup
import pandas as pd


cols = ['name','code','3_month','1_year','5_year']
df = pd.DataFrame(columns=cols)

'''
Enter the number of pages you want to crawl
The program will export result to coin_prediction.csv
'''
pages = 5
for page in range(1, pages+1):
    res = requests.get(f'https://walletinvestor.com/forecast?page={page}&per-page=100')
    soup = BeautifulSoup(res.text, 'lxml')

    data = []
    for tag in soup.find_all('tr','w0'):
        c_name = tag.find('td',{'data-col-seq':'0'}).find('a').find(text=True)
        c_code = tag.find('td',{'data-col-seq':'0'}).find('div').text
        c_3_month = tag.find('td',{'data-col-seq':'2'}).find('a').text
        c_1_year = tag.find('td',{'data-col-seq':'3'}).find('a').text
        c_5_year = tag.find('td',{'data-col-seq':'4'}).find('a').text
        row = dict(zip(cols, [c_name, c_code, c_3_month, c_1_year, c_5_year]))
        data.append(row)
    
    df = df.append(data, True)

df.to_csv('coin_prediction.csv', index=False)