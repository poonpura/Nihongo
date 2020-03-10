"""
This module contains all the functions designed for use by the client.

See README file for information on how to use.

Author: Pura Peetathawatchai
"""

import freq_dict
import web_scrape

"""
Returns the frequency dictionary of the textual contents of '```filename```.txt'.

Precondtion: '```filename```.txt' only contains the Japanese text to be analyzed.
"""
def dict_of_file(filename):
    return freq_dict.f(freq_dict.from_file(filename))

"""
Returns the frequency ranking of the textual contents of '```filename```.txt'.

Precondtion: '```filename```.txt' only contains the Japanese text to be analyzed.
"""
def rank_of_file(filename):
    return freq_dict.f_rank(freq_dict.from_file(filename))

"""
Returns the frequency dictionary of the textual contents of ```URL```.

If ```deepsearch``` is True, performs a recursive analysis on every child
webpage. The default value is False.
"""
def dict_of_web(url, deepsearch=False):
    return web_scrape.tree_dict(url) if deepsearch else web_scrape.dict(url)

"""
Returns the frequency ranking of the textual contents of ```URL```.

If ```deepsearch``` is True, performs a recursive analysis on every child
webpage. The default value is False.
"""
def rank_of_web(url, deepsearch=False):
    return web_scrape.tree_rank(url) if deepsearch else web_scrape.rank(url)

"""
Exports ```data``` as the csv file 'data.csv' in the directory. If such a file
already exists, its contents are overwritten.

Precondition: ```data``` is a list for the frequency ranking or a frequency
dictionary.
"""
def to_csv(data):
    import pandas as pd
    if type(data) == dict:
        words, frequencies = list(data.keys()), list(data.values())
        d = {'word': words, 'frequency': frequencies}
    else:
        d = data
    df = pd.DataFrame(data=d)
    df.to_csv("./data.csv", sep=',', header=False, index=False)
