"""
Code to extend word frequency analysis to Internet-based sources.

Makes use of Selenium Webdriver (ChromeDriver).

Author: Pura Peetathawatchai
"""

import string
from selenium import webdriver
import freq_dict

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# Set path name to be path to webdriver
browser = webdriver.Chrome("/Users/Pura/Documents/chromedriver", chrome_options=options)

"""
Removes all Roman characters and punctuation from ```text``` so that only
Japanese characters and numbers remain. English characters are irrelevant to
word frequency analysis anyway. Intended for use to extract Japanese characters
from an HTML string.
"""
def deromanize(text):
    acc= ''
    length = len(text)
    for i in range(length):
        if not text[i] in string.punctuation + string.ascii_letters:
            acc= acc + text[i]
    return acc

"""
Returns the HTML string of the web page given by ```URL```.
"""
def get_html(url):
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html

"""
(HELPER)
Applies ```f``` on the string of Japanese words extracted from the web page
given by ```URL```.
"""
def on_url(f, url):
    html = get_html(url)
    raw_txt = deromanize(html)
    return f(raw_txt)

"""
Returns the frequency dictionary of the textual contents of ```URL```.
"""
def dict(url):
    return on_url(lambda x: freq_dict.f(x), url)

"""
Returns the frequency ranking of the textual contents of ```URL```.
"""
def rank(url):
    return on_url(lambda x: freq_dict.f_rank(x), url)
