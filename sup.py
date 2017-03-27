import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import sys
import time
from datetime import datetime

product = "Work Pant"

style = "Pink"
size = "32"
mainUrl = "http://www.supremenewyork.com/shop/all/pants"
baseUrl = "http://supremenewyork.com"
checkoutUrl = "https://www.supremenewyork.com/checkout"
namefield = "Donald Trump"
emailfield = "trump@trump.com"
phonefield = "0000000000"
addressfield = "1 Pennsylvania rd"
cityfield = "Washington DC"
zipfield = "00000"
statefield = "DC"
cctypefield = "Mastercard"  # "master" "visa" "american_express"
ccnumfield = "0000000000000000"  # Randomly Generated Data (aka, this isn't mine)
ccmonthfield = "00"  # Randomly Generated Data (aka, this isn't mine)
ccyearfield = "2121"  # Randomly Generated Data (aka, this isn't mine)
cccvcfield = "999"  # Randomly Generated Data (aka, this isn't mine)


def find():
    print("Trying to find link")
    r = requests.get(mainUrl).text
    if product in r:
        print("found prod")
        getLink(r)
    else:
        return
        
def getLink(r):
    print("BSing link out of text")
    soup = BeautifulSoup(r, "html.parser")
    #print(soup.prettify
    link1 = "empty"
    link2 = "alsoempty"
    for a in soup.find_all('a', href=True):
        if product in a:
            link1 = a['href']
            if (style == ""):
                buy(link1)
            
        if style in a:
            link2 = a['href']
        if (link1 == link2):
            buy(link1)
            
            
def buy(l):
    prdlink = baseUrl + l
    
    driver.get(prdlink)
    #select = Select(driver.find_element_by_id("size"))
    #select.select_by_visible_text(size)
    
    
    driver.find_element_by_name("commit").click()
    driver.find_element_by_link_text("checkout now").click()
    driver.find_element_by_id("order_billing_name").send_keys(namefield)
    driver.find_element_by_id("order_email").send_keys(emailfield)
    driver.find_element_by_id("order_tel").send_keys(phonefield)
    driver.find_element_by_id("bo").send_keys(addressfield)
    driver.find_element_by_id("order_billing_city").send_keys(cityfield)
    driver.find_element_by_id("order_billing_zip").send_keys(zipfield)
    select = Select(driver.find_element_by_id("order_billing_state"))
    select.select_by_visible_text(statefield)
    select = Select(driver.find_element_by_id("credit_card_type"))
    select.select_by_visible_text(cctypefield)
    driver.find_element_by_id("cnb").send_keys(ccnumfield)
    driver.find_element_by_id("vval").send_keys(cccvcfield)
    select = Select(driver.find_element_by_id("credit_card_month"))
    select.select_by_visible_text(ccmonthfield)
    select = Select(driver.find_element_by_id("credit_card_year"))
    select.select_by_visible_text(ccyearfield)
    
    
    
    element = driver.find_element_by_css_selector(".terms")
    element.click()
    
   # This line commented out to prevent stupid people from buying something by mistake. Uncomment only if you know what you are doing.
   # driver.find_element_by_name("commit").click()  
    
    t1 = time.time()
    print("took " + str(t1-t0) + " to check out")
    print("Process payment clicked, rest is up to supreme.")
    sys.exit(0)

i = 0
driver = webdriver.Chrome()
driver.implicitly_wait(1)


print("Webdriver started")
print ("Current time is " + str(datetime.now().time()))
go = input("Type go to begin\n")

while (go == "go"):
    t0 = time.time()
    find()
    print("on try number" + str(i))
    i=i+1
    time.sleep(3)
