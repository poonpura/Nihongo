"""
Code to generate a Japanese word frequency dictionary.

The aim of this module is to take in a Japanese language string as input and
output the occurence frequencies of different Japanese words.

Makes use of the CaboCha Japanese NLP module by Taku Kudo. Thus, installation
of CaboCha is a prerequisite to using this module. For more information see:
https://rstudio-pubs-static.s3.amazonaws.com/462850_98582068058d4191a70b7246d2ceee29.html

Also requires Naked module. To install, run ```pip install Naked``` in the
command line.

Loosely inspired by methodology in "A Frequency Dictionary of Japanese" by
Tono et al.

Author: Pura Peetathawatchai
"""

import cabocha
from cabocha.analyzer import CaboChaAnalyzer
analyzer = CaboChaAnalyzer()
from Naked.toolshed.shell import execute_js, muterun_js
import json

"""
Returns a token stream (type: string list) of ```text```. A phrase token
is either a noun, verb or adjective phrase or a particle. Ignores punctuation
and spacing.

Parameters:
```text``` : ```str```
"""
def lex(text):
    tree = analyzer.parse(text)
    stream = []
    for chunk in tree:
        for token in chunk:
            stream.append(_extr(token))
    _regroup(stream)
    return stream

"""
(Helper)

Extracts the string from the ```Token``` object.

Uses string slicing methods which is not preferred but unavoidable due to lack
of accessible documentation in CaboCha module.
"""
def _extr(token):
    rep = repr(token)
    i1 = rep.index('"')
    i2 = rep.index('"', i1 + 1)
    return rep[i1 + 1:i2]

"""
(Helper)

Reorganizes the token stream to include the 'て'/'で' as part of the token of
a verb in 'ーて' form.
"""
def _regroup(stream):
    if stream[0] in {'て', 'で', 'た', 'だ'}:
        return stream[0] + _regroup(stream[1:])
    def _del_t(stream, hira):
        while hira in stream:
            i = stream.index(hira)
            stream[i - 1]= stream[i - 1] + hira
            stream.remove(hira)
    _del_t(stream, 'て')
    _del_t(stream, 'た')
    def _del_d(stream, hira):
        try:
            i = stream.index(hira)
            if len(stream[i - 1]) > 1 and stream[i - 1][-1] == 'ん':
                stream[i - 1]= stream[i - 1] + hira
                stream.remove(hira)
                _del_d(stream, hira)
            else:
                tl = stream[i + 1:]
                _del_d(tl, hira)
                stream[i + 1:] = tl
        except ValueError:
            pass
    _del_d(stream, 'で')
    _del_d(stream, 'だ')

"""
Returns the deconjugated verb base of ```verb```.

This function utilizes Naked to run the Japanese verb deconjugator module by
https://github.com/mistval in JavaScript. The console output is intercepted,
stored as a variable, then processed locally.

Precondition: ```verb``` is a valid Japanese verb.
"""
def deconjugate(verb):
    naked_object = muterun_js('deconjugator.js', verb)
    jstr = naked_object.stdout.decode("utf-8")
    jobj = json.loads(jstr)
    return jobj[0]["base"]
