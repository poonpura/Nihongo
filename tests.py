"""
Test cases for freqency dictionary module.

Author: Pura Peetathawatchai
"""

from freq_dict_d1 import *
import freq_dict_d1

x = first_occ(["a", "b"], "")

def test_p_lexer():
    print("Testing p_lexer and helpers")

    print("Testing first_occ")
    # empty string
    assert first_occ(["a", "b"], "") == -1
    # all letters occur
    assert first_occ(["a", "b", "c"], "defcba") == 3
    # not all letters occur
    assert first_occ(["x", "y", "z", "r"], "abxfgz") == 2
    # none of the letters occur
    assert first_occ(["a", "x"], "Wyvern lords suck") == -1

    print("Testing p_lexer")
    # string with no punctuation or spaces
    txt = "最終決戦においてファウダーに操られクロムを殺害し"
    output = ["最終決戦","に","おいてファウダー","に","操られクロム","を","殺害し"]
    assert p_lexer(txt) == output
    # keeps "ーんで" verb as one token
    txt = "本を読んでいる"
    output = ["本","を","読んでいる"]
    assert p_lexer(txt) == output
    # recognizes "で" particle
    txt = "公園で遊ぶ"
    output = ["公園","で","遊ぶ"]
    assert p_lexer(txt) == output
    # string with punctuations and spaces
    txt = "シミュレーションRPG『ファイアーエムブレム 覚醒』のもう一方の主人公である「マイユニット」のデフォルト名。"
    output = ["シミュレーションRPG", "ファイアーエムブレム", "覚醒", "の", "もう一方",
    "の", "主人公", "で", "ある", "マイユニット", "の", "デフォルト名"]
    assert p_lexer(txt) == output
    print("p_lexer: PASS!")

test_p_lexer()
