import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome","firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver= webdriver.Chrome()

    elif request.param == "firefox":
        web_driver= webdriver.Firefox()
    else:
        raise "Browser Not Found!"
    web_driver.maximize_window()
    web_driver.get("https://workspace.google.com/intl/en-US/gmail/")
    web_driver.implicitly_wait(10)
    request.cls.driver= web_driver

    yield
    web_driver.quit()