"""Example module."""

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def execute():
    """Just an selenium example to execute on lambda."""
    logging.info('Starting')
    driver = webdriver.Firefox(log_path='/tmp/geckodriver.log')
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    execute()