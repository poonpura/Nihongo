"""
Code to extend word frequency analysis to Internet-based sources.

Makes use of <web_scraper>.

Author: Pura Peetathawatchai
"""

import string

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
