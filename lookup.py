"""
Module with helper functions to help with extracting information from relevant
areas of the internet. Intended to specifically support other modules in this
project.

Makes use of the Selenium Chrome driver. Thus, some functions in this module
will open the Google Chrome browser to carry out certain procedures.

Prerequisites:
Google Chrome version 80.0.3987.87
Selenium webdriver for Chrome with PATH specified.
For more information on installing driver, see:
https://pypi.org/project/selenium/

Author: Pura Peetathawatchai
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Returns True if [word] is a [valid] word in JMdictDB, False otherwise.

Uses Chrome to look up the word on the online JMdictDB website, which may be
time consuming. Processing time for one word can take up to 5-10 seconds, so
faster alternatives might be preferred. Program may not work if the JMdictDB
website source code has been updated.

Precondition: [word] contains only Japanese characters.
"""
def is_valid_word(word):
    browser = webdriver.Chrome() # set to be path to your chromedriver.exe
    from selenium.webdriver.support.ui import Select

    browser.get('http://edrdg.org/jmdictdb/cgi-bin/srchformq.py?svc=jmdict&sid=&')
    assert browser.title == 'JMdictDB - Basic Search'

    select = Select(browser.find_element_by_name('y1'))
    select.select_by_visible_text("Is")
    search = browser.find_element_by_id('t1')  # Find the search box
    search.send_keys(word + Keys.RETURN)

    wait = WebDriverWait(browser, 10)
    wait.until(lambda x: EC.title_is('JMdictDB - Entries') or EC.title_is('JMdictDB - Search results'))
    out_src = browser.page_source
    browser.quit()

    return not ('No entries found.' in out_src)
