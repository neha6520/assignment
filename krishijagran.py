import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome('/home/neha/Downloads/chromedriver')
driver.get('https://krishijagran.com/news')
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

link = []
results = soup.find_all(class_='img')
for link_elem in results:
    #  print(link_elem['href'])
    link.append(link_elem['href'])

News = []
results1 = soup.find_all(class_="nc-item shadow-sm")
for news_elem in results1:
    x = news_elem.text
    text = os.linesep.join([s for s in x.splitlines() if s])
    #  print(text)
    News.append(text)

df = pd.DataFrame(columns=['News', 'Link'])
for l in range(len(News)):
    df.loc[len(df.index)] = [News[l], link[l]]

print(df)

df.to_csv('Output.csv', index=False)

driver.quit()