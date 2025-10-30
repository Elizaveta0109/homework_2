import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()

def test_github_open(driver):
    url = "https://github.com/"
    driver.get(url)
    assert driver.title == 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'
    assert driver.current_url == url