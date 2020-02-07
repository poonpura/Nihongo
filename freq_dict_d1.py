"""
First draft of Japanese word frequency dictionary.

The aim of this module is to take in a Japanese language string as input and
output the occurence frequencies of different Japanese words.

Loosely inspired by methodology in "A Frequency Dictionary of Japanese" by
Tono et al.

Author: Pura Peetathawatchai
"""

# CONSTANTS
HIRAGANA = ["あ","い","う","え","お","か","が","き","ぎ","く","ぐ","け","げ","こ",
"ご","さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","つ","づ",
"て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ",
"ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め","も","や","ゆ","よ","ら","り",
"る","れ","ろ","わ","を"]
PARTICLES = ["は","が","の","を","に","へ","で"]
PUNCTUATION = ["。","、","「","」","！","？","￥","＠","＃","＄","％","＾","＆","＊",
"（","）","ー","＿","＝","＋","『","』","｜","：","；","’","”","＜","＞"]

"""
Returns a phrase token stream (type: string list) of [text]. A phrase token
is either a noun, verb or adjective phrase or a particle. Ignores punctuation
and spacing.

Precondition: [text] is a string containing only Japanese characters. All words/
phrases which can be written in Kanji should be written in Kanji rather than
Hiragana or Katakana.
"""
def p_lexer(text):
    if text == "":
        return []
    dividers = PARTICLES + PUNCTUATION + [" "] + ["　"]
    dividers.remove("ー")
    idx = first_occ(dividers, text)
    def helper(text, idx):
        if idx == -1:
            return [text]
        if idx == 0:
            char = text[0]
            if char in PARTICLES:
                return [text[0]] + p_lexer(text[1:])
            else:
                return p_lexer(text[1:])
        if text[idx - 1: idx + 1] == "んで":
            idx2 = first_occ(dividers, text, idx + 1)
            return helper(text, idx2)
        return [text[:idx]] + p_lexer(text[idx:])
    return helper(text, idx)

"""
(Helper)

Returns the index of the first occurence of any of the characters in [lst] in
[[str[start + 1:]] and -1 if none of the characters in [lst] occur in said
substring.

Precondition: [lst] is a non-empty list of 1-character strings.
"""
def first_occ(lst, str, start=0):
    idxs = list(map(lambda c: str.find(c, start), lst))
    len_ = len(str)
    for i in range(len(idxs)):
        if idxs[i] == -1:
            idxs[i] = len_
    min_ = min(idxs)
    if min_ == len(str):
        return -1
    else:
        return min_
