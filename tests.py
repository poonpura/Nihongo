"""
Test script for freqency dictionary module.

Author: Pura Peetathawatchai
"""

from freq_dict import *
from lookup import *

def test_lexer():
    print("Testing lexer")
    # merges -te form
    assert lex("どうぞ食べて下さい") == ["どうぞ","食べて","下さい"]
    # merges past form
    assert lex("ご飯もう食べた") == ["ご飯","もう","食べた"]
    assert lex("公園で遊んだ") == ["公園","で","遊んだ"]
    # merges adjective -te form
    assert lex("長くて綺麗で") == ["長くて","綺麗","で"]
    # merges nasalied verb -te form
    assert lex("本を読んでいる") == ["本","を","読んで","いる"]
    # handles both cases
    print(lex("公園で遊んでいる"))
    assert lex("公園で遊んでいる") == ["公園","で","遊んで","いる"]
    # test with long authentic text
    text = "作者が最も長く描き続けた代表作であり、日本では国民的な漫画作品の一つ。"
    output = ['作者','が','最も','長く','描き','続けた','代表','作','で','あり','、',
    '日本','で','は','国民','的','な','漫画','作品','の','一つ','。']
    assert lex(text) == output
    text = "1980年からはアニメーション映画の原作として長編の執筆を開始し、これを『大長編ドラえもん』と称している。"
    output = ['1980','年','から','は','アニメーション','映画','の','原作','として','長編',
    'の','執筆','を','開始','し','、','これ','を','『','大','長編','ドラえもん','』','と',
    '称して','いる','。']
    assert lex(text) == output
    print("lex: PASS!")

def test_lookup():
    print("Testing helper functions from the [lookup] module. May be time consuming.")
    print("Testing is_valid_word")
    assert is_valid_word("食べる") == True
    assert is_valid_word("食べ") == False
    assert is_valid_word("アルバイト") == True
    assert is_valid_word("食べられる") == True
    print("is_valid_word: PASS!")

test_lexer()
test_lookup()
