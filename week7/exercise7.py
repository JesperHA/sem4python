import bs4
import requests
from selenium import webdriver
from time import sleep
import matplotlib.pyplot as plt


browser = webdriver.Chrome("./chromedriver.exe")


def s1():
    url = "https://www.merchbar.com/"
    browser.get(url)

    browser.implicitly_wait(3)

    search_field = browser.find_element_by_css_selector("input.typeahead.tt-input")
    search_field.send_keys('breaking benjamin\n')

    browser.implicitly_wait(3)

    html = browser.page_source

    data = html.text

    soup = bs4.BeautifulSoup(data, 'html.parser')
    el = soup.find_all('div', class_="mb-3")
    print(el)


def s2():
    url = 'https://www.merchbar.com/search?q=breaking%20benjamin&p=1'
    browser.get(url)
    browser.implicitly_wait(1)

    checkbox = browser.find_elements_by_class_name('ais-RefinementList-labelText')[2]
    checkbox.click()
    sleep(2)
    cd1 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[2]/div[2]/div[1]/div/div/a[2]/div[1]')
    cd1.click()
    sleep(2)
    track_list = browser.find_element_by_class_name('track-list')
    tracks = track_list.find_elements_by_class_name('track')
    print(len(tracks))

def s3():

    url = 'https://www.merchbar.com/search?q=breaking%20benjamin&p=1'
    browser.get(url)
    browser.implicitly_wait(1)

    all_items = 0
  

    amount_str = '//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/div[1]/span'


    #Finder alle items
    all_items = browser.find_element_by_xpath(amount_str).text[:2]

    print(all_items)
    sleep(2)


    expand_menu = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/button[2]')
    expand_menu.click()
    sleep(2)

    checkbox_benja = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/div[5]/div/ul/li[5]/label/span[1]')
    checkbox_benja.click()
    sleep(2)
    true_benja = browser.find_element_by_xpath(amount_str).text[:2]
    print(true_benja)

    checkbox_sale = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/div[2]/label/span')
    checkbox_sale.click()
    sleep(2)
    sale_benja = browser.find_element_by_xpath(amount_str).text[:2]
    print(sale_benja)
    sleep(2)
    checkbox_sale.click()

    expand_menu2 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/button[6]')
    expand_menu2.click()
    sleep(2)

    checkbox_availability = browser.find_element_by_xpath('//*[@id="__next"]/div/div[4]/div/div[5]/div[1]/div[9]/div/ul/li[2]/label/span[1]')
    checkbox_availability.click()
    sleep(2)
    avail_benja = browser.find_element_by_xpath(amount_str).text[:2]
    print(avail_benja)

    all_items = int(all_items)
    true_benja = int(true_benja)
    sale_benja = int(sale_benja)
    avail_benja = int(avail_benja)

    true_pct = true_benja/all_items * 100
    sale_pct = sale_benja/all_items * 100
    avail_pct = avail_benja/all_items * 100

    

    data = {'True benjamin': true_pct, 'on sale': sale_pct,
            'out of stock': avail_pct}

    plt.bar(data.keys(), data.values())
    plt.ylim([0, 100])
    plt.title('Breaking Benjamin merchandise', fontsize=12)
    plt.ylabel('Percentage', fontsize=10)
    plt.show()

s3()




