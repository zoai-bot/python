
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import re
import numpy as np
import matplotlib.pyplot as plt

source_url = "http://namu.wiki/RecentChanges"

req = requests.get(source_url)
html = req.content
soup = BeautifulSoup(html, 'lxml')
contents_table = soup.find(name="table")
table_body = contents_table.find(name='tbody')
table_rows = table_body.find_all(name="tr")

page_url_base = "http://namu.wiki"
page_urls = []
for index in range(0, len(table_rows)):
    first_td = table_rows[index].find_all('td')[0]
    td_url = first_td.find_all('a')
    if len(td_url) > 0:
        page_url = page_url_base + td_url[0].get('href')
        if 'png' not in page_url:
            page_urls.append(page_url)
page_urls = list(set(page_urls))
print(page_urls)

from selenium import webdriver

driver = webdriver.Chrome("C:\ProgramData\Anaconda3\Lib\site-packages\selenium\chromedriver")

my_pw = "----본인 패스워드 입력하세요----"
driver.find_element_by_name('password').send_keys(my_pw)
driver.find_element_by_css_selector('button.btn_login').click()