"""
Code to extend word frequency analysis to Internet-based sources.

Makes use of the Selenium Chrome driver. Thus, some functions in this module
will open the Google Chrome browser to carry out certain procedures.

Prerequisites:
Google Chrome version 80.0.3987.87
Selenium webdriver for Chrome with PATH specified (see line 26)
For more information on installing driver, see:
https://pypi.org/project/selenium/

Author: Pura Peetathawatchai
"""

import string
from selenium import webdriver
import freq_dict
import copy

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# Set path name to be path to webdriver
def init_browser():
    return webdriver.Chrome("/Users/Pura/Documents/chromedriver", chrome_options=options)

"""
Removes all Roman characters and punctuation from ```text``` so that only
Japanese characters and numbers remain. English characters are irrelevant to
word frequency analysis anyway. Intended for use to extract Japanese characters
from an HTML string.
"""
def _deromanize(text):
    acc= ''
    length = len(text)
    for i in range(length):
        if not text[i] in string.punctuation + string.ascii_letters:
            acc= acc + text[i]
    return acc

"""
Returns the HTML string of the web page given by ```URL```.
"""
def _get_html(url):
    browser = init_browser()
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html

"""
Applies ```f``` on the string of Japanese words extracted from the web page
given by ```URL```.
"""
def _on_url(f, url):
    html = _get_html(url)
    raw_txt = _deromanize(html)
    return f(raw_txt)

"""
Returns the frequency dictionary of the textual contents of ```URL```.
"""
def dict(url):
    return _on_url(lambda x: freq_dict.f(x), url)

"""
Returns the frequency ranking of the textual contents of ```URL```.
"""
def rank(url):
    return _on_url(lambda x: freq_dict.f_rank(x), url)

def _add(d1, d2):
    d= copy.deepcopy(d1)
    for k in d2.keys():
        if (k in d.keys()):
            d[k]= d[k] + d2[k]
        else:
            d[k]= d2[k]
    return d

def tree_dict(url):
    def tree_dict_acc(url, acc):
        if url in acc:
            return {}, acc

        browser = init_browser()
        browser.get(url)
        r_url = browser.current_url
        elems = set(browser.find_elements_by_xpath("//*[contains(@href,'"+r_url+"')]"))
        acc= acc + [r_url]

        link_lst= []
        for elem in elems:
            link_lst.append(elem.get_attribute("href"))
        links = set(link_lst)

        dict= freq_dict.f(_deromanize(browser.page_source))
        browser.quit()
        for link in links:
            xtr, acc= tree_dict_acc(link, acc)
            dict= _add(dict, xtr)

        return dict, acc

    dict, _ = tree_dict_acc(url, [])
    return dict

print(tree_dict("https://www.nintendo.co.jp/"))
