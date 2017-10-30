from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import re
from Maoyantop100.gene import Gene

def get_first_page(browser,string):
    try:
        select = Select(browser.find_element_by_id('database'))
        select.select_by_value('gene')
        input = browser.find_element_by_id('term')
        input.send_keys(string)
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'navcontent')))
        html = browser.page_source;
        return html;
    except Exception:
        return None

def get_pages(browser,string):
    input_page = browser.find_element_by_id('pageno')
    input_page.clear()
    input_page.send_keys(string)
    input_page.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'navcontent')))
    html = browser.page_source;
    return html;

def parse_first_page(html):
    soup = BeautifulSoup(html, 'lxml')
    count = soup.select('.result_count.left')[0].text
    pattern = re.compile('.*of (\d+)')
    summary = re.findall(pattern,count)
    page = int(soup.find_all(id='pageno')[0].attrs['last'])
    if summary[0] != '':
        return int(summary[0]),page
    return None

def parse_pages(html,genes):
    soup = BeautifulSoup(html,'lxml')
    lis = str(soup.find_all('tbody')[0])
    pattern = re.compile('<tr.*?<td.*?<div>.*?href="(.*?)".*?>(.*?)</a>.*?<span.*?ID: (\d*).*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td.*?>(\d*)</td>.*?</tr>',re.S)
    results = re.findall(pattern, lis)
    for result in results:
        url, name, id, desc, location, aliases, mim = result
        desc = re.sub('<.*?>', '', desc)
        gene = Gene(url, name, id, desc, location, aliases, mim)
        genes.append(gene)
    return genes

def main():
    browser = webdriver.Chrome()
    genes = []
    try:
        url = 'https://www.ncbi.nlm.nih.gov/'
        browser.get(url)
        html = get_first_page(browser,'heart disease')
        count,pages = parse_first_page(html)
        if count > 100:
            for i in range(5):
                htmls = get_pages(browser,i+1)
                parse_pages(htmls,genes)
        else:
            for i in range(pages):
                htmls = get_pages(browser, i + 1)
                parse_pages(htmls, genes)
        for gene in genes:
            print(gene.name)
        print(len(genes))




    finally:
        browser.close()

if __name__ == '__main__':
    main()