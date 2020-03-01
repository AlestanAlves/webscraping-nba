import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
option.headless = True 
driver = webdriver.Firefox() # se eu tirar o headless consigo ver o processo acontecendo

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

#print(html_content) todo o conteudo html da pag

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html( str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYE R', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

top10ranking = {}

print(df)

driver.quit()
