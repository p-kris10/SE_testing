from search import WorkspaceLoginPage
import time 
import random
import pytest

def test_login(browser):
  home_page = WorkspaceLoginPage(browser)
  home_page.load()
  username = home_page.login("kristen.pereira@spit.ac.in","12345678")
  time.sleep(2)
  assert username == "kris10"

def test_invalid_login(browser):
  home_page = WorkspaceLoginPage(browser)
  home_page.load()
  msg = home_page.login_("asdfsadfsdf@dfsd.com","12345678")
  time.sleep(2)
  assert "Errors" in msg



def test_add_subspace(browser):
  home_page = WorkspaceLoginPage(browser)
  home_page.load()
  name = "WWE" +str(random.randint(0,100)) 
  username = home_page.login("kristen.pereira@spit.ac.in","12345678")
  test_name = home_page.add_subspace(name)
  test_name =test_name[2:]
  time.sleep(2)
  assert name == test_name

def test_chat_send(browser):
  user = WorkspaceLoginPage(browser)
  user.load()
  user.login("kristen.pereira@spit.ac.in","12345678") 
  test_msg = "test" + str(random.randint(0,100))
  user.send_message(test_msg)
  time.sleep(1)
  recvd_msg = user.get_latest_msg()
  pytest.msg = test_msg
  time.sleep(3)
  assert test_msg == recvd_msg


def test_chat_recv(browser):
  user = WorkspaceLoginPage(browser)
  user.load()
  user.login("aman.parikh@spit.ac.in","12345678") 
  recvd_msg= user.get_latest_msg()
  time.sleep(3)
  assert "test" in recvd_msg