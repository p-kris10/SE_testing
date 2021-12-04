from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WorkspaceLoginPage:

  URL = 'http://127.0.0.1:3000/'

 # element search queries
  USER_NAME = (By.NAME, 'email')
  PASS = (By.NAME, 'password')
  LOGIN = (By.CLASS_NAME,'button')


  def __init__(self, browser):
    self.browser = browser


#functions used in testing
  def load(self):
    self.browser.get(self.URL)

  def sign_out(self):
    singout = self.browser.find_element(By.CLASS_NAME,"dropdown")
    singout.click()
    btn = self.browser.find_element(By.CLASS_NAME,"visible")
    inn = btn.find_element(By.TAG_NAME,"span")
    inn.click()

  def login_(self, user,pswrd):
    username = self.browser.find_element(*self.USER_NAME)
    password = self.browser.find_element(*self.PASS)
    username.send_keys(user)
    password.send_keys(pswrd)
    login = self.browser.find_element(*self.LOGIN)
    login.click()
    time.sleep(3)
    msg = self.browser.find_element(By.CLASS_NAME,"error")
    return msg.text

  def login(self, user,pswrd):
    username = self.browser.find_element(*self.USER_NAME)
    password = self.browser.find_element(*self.PASS)
    username.send_keys(user)
    password.send_keys(pswrd)
    login = self.browser.find_element(*self.LOGIN)
    login.click()
    time.sleep(3)
    avatar = self.browser.find_element(By.TAG_NAME,"span")
    return avatar.text

  def add_subspace(self,test):
    add = self.browser.find_element(By.CLASS_NAME,"add-s")
    add.click()
    time.sleep(2)
    name = self.browser.find_element(By.NAME,"name")
    save = self.browser.find_element(By.CLASS_NAME,"checkmark")
    name.send_keys(test)
    save.click()
    spaces = self.browser.find_elements(By.ID,"style2")
    check = spaces[-1].text
    return check


  def send_message(self,msgg):
    msg = self.browser.find_element(By.NAME,"message")
    msg.send_keys(msgg)
    send = self.browser.find_element(By.CLASS_NAME,"send")
    send.click()
   
  def get_latest_msg(self):
    msgs = self.browser.find_elements(By.CLASS_NAME,"content")
    msg_text = msgs[-1].find_element(By.CLASS_NAME,"text")
    return msg_text.text


    
