from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class FlipkartResultPage:
  
 

  URL  = 'https://www.flipkart.com/oppo-a83-champagne-16-gb/p/itmfawnctfqfgxtj?pid=MOBFAWNCGKHSEMRD&lid=LSTMOBFAWNCGKHSEMRDIPIHH0&marketplace=FLIPKART&q=oppo&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=54531962-a586-47c5-ac2e-f8f79adc49d3.MOBFAWNCGKHSEMRD.SEARCH&ppt=sp&ppn=sp&ssid=u30hshea280000001638332767097&qH=c892ba238c98835d'
  SEARCH_INPUT = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')

  @classmethod
  def PHRASE_RESULTS(cls, phrase):
    return (By.CLASS_NAME,'_4rR01T')

  

  def __init__(self, browser):
    self.browser = browser
  
  def result_count_for_phrase(self, phrase):
    res= self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
    result = []
    for i in res:
      if phrase in i.text:
        result.append(i)
    
    return len(result)
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    return search_input.get_attribute('value')

  def title(self):
    return self.browser.title

  def set_filter(self):
    xpath = "//div[@class='_3uDYxP']/select[@class='_2YxCDZ']"
    price = Select(self.browser.find_element(By.XPATH,xpath));
    sel_price = price.options
    price.select_by_index(2)
    time.sleep(2)
    return int(sel_price[2].text[1:])

  def get_prices(self):
   
    prices = self.browser.find_elements(By.CLASS_NAME,'_30jeq3 _1_WHN1')
    final = []
    for price in prices:
      final.append(int(price.text[1:]))
    return final

  def load_item_page(self):
    self.browser.get(self.URL)

  def add_to_cart(self):
    btn = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
    btn.click()
    time.sleep(2)
    cart = self.browser.find_element(By.CLASS_NAME,'_3g_HeN')
    cart = cart.text.replace("("," ")
    cart = cart.replace(")"," ")
    num = 0
    for i in cart.split():
      if i.isdigit():
        num = i
    
    return int(num)

  def remove_cart(self):
    btn = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div[3]/div[2]/div[2]')
    btn.click()
    time.sleep(2)
    rbtn = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div[2]')
    rbtn.click()
    time.sleep(2)
    msg = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]')
    return msg.text




    

    
