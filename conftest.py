import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture
def browser():
    b = Service("C:\\edgedriver_win64\\msedgedriver.exe")
    b = webdriver.Edge(service = b)
    b.implicitly_wait(10)
    yield b
    b.quit()
