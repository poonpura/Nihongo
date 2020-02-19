"""
Code to generate a Japanese word frequency dictionary.

The aim of this module is to take in a Japanese language string as input and
output the occurence frequencies of different Japanese words.

Makes use of the CaboCha Japanese NLP module by Taku Kudo. Thus, installation
of CaboCha is a prerequisite to using this module. For more information see:
https://rstudio-pubs-static.s3.amazonaws.com/462850_98582068058d4191a70b7246d2ceee29.html

Author: Pura Peetathawatchai
"""

import string
import copy
import cabocha
from cabocha.analyzer import CaboChaAnalyzer
analyzer = CaboChaAnalyzer()

# CONSTANTS
HIRAGANA = ["あ","い","う","え","お","か","が","き","ぎ","く","ぐ","け","げ","こ",
"ご","さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","つ","づ",
"て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ",
"ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め","も","や","ゆ","よ","ら","り",
"る","れ","ろ","わ","を", "っ"]
PUNCTUATION = ["。","、","「","」","！","？","￥","＠","＃","＄","％","＾","＆","＊",
"（","）","ー","＿","＝","＋","『","』","｜","：","；","’","”","＜","＞", "・"] + \
list(string.punctuation)

"""
Returns the dictionary that maps each token base in ```text``` to their
respective occurence frequency.

The string is broken down into a stream of tokens by CaboCha. Each token is then
deconjugated to yield their base form.

Bound functional morphemes and particles are also considered as tokens by this
function, so further processing of the output dictionary may be neccessary.
"""
def raw_freq(text):
    tree = analyzer.parse(text)
    stream = []
    for chunk in tree:
        for token in chunk:
            base = token.feature_list[-3]
            stream.append(base)

    dict = {}
    for token in stream:
        if token in dict.keys():
            dict[token]= dict[token] + 1
        else:
            dict[token] = 1

    return dict

"""
Returns a copy of ```dict``` with all keys (tokens) containing only hiragana or
punctuation removed.
"""
def clean(dict):
    output = {}
    for token in dict.keys():
        if not all(c in HIRAGANA + PUNCTUATION for c in list(token)):
            output[token] = dict[token]

    return output

"""
Returns the dictionary that maps each token base in ```text``` to their
respective occurence frequency, ommitting tokens containing only hiragana or
punctuation.
"""
def freq_dict(text):
    return clean(raw_freq(text))

"""
Returns a list of vocabulary (ommitting hiragana-only terms and particles) that
occur in ```text```, sorted by descending frequency
"""
def freq_rank(text):
    dict = freq_dict(text)
    return sorted(dict, key = dict.get, reverse = True)

"""
Returns a string containing the contents of ```file``` with '\n' characters
removed.

Precondition: ```file``` is a .txt file.
"""
def from_file(filename):
    file = open(filename, 'r')
    text = file.read().replace('\n', '')
    return text
