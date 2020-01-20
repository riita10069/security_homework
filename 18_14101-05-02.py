import string
import random


def make_random():
    li = list(string.ascii_letters)
    li[len(li): len(li)] = [" ", ",", '.', "-"]
    li = random.sample(li, len(li))
    return li
# ランダムな並びの重複しない文字列を発生


def make_dictionary():
    dic = {}
    plain = make_random()
    ran_char = random.sample(make_random(), len(plain))
    for i in range(len(plain)):
        dic[plain[i]] = ran_char[i]
    return dic
# 辞書の作成


def count_char(dic, sentence):
    li = dic.keys()
    count_dic = {}
    for char in li:
        count_dic[char] = sentence.count(char)
    return count_dic


if __name__ == '__main__':

    dic = make_dictionary()
    encode = []

    print("INPUT:")
    # 文字列の入力
    sentence = "In our previous work, we proposed a biometric authentication method using a secure imaging system that was based on compressed sensing. In this approach, although we can acquire an encrypted vein image, the verification process requires the restoration of the raw finger-vein image. To address this issue, we propose an improved authentication method that we can verify alternate biometric features from which it is difficult to restore the original finger-vein image by introducing the permutation matrix for randomizing the object signal. Numerical simulations show that our method has favorable accuracy, although it exhibits a slightly degraded accuracy in comparison with that of the conventional method that uses a raw finger-vein image. "
    print("plain:")
    print(sentence)

    # 暗号文の作成
    for char in range(len(sentence)):
        encode.append(dic[sentence[char]])

    # 分布数を作成
    new_dic = count_char(dic, encode)
    # 要素数順に並び替え
    score_sorted = sorted(new_dic.items(), key = lambda x : x[1])

    print("OUTPUT:")

    # 分布数を表示
    for key in score_sorted:
        print(key)

    # 問題点は文字の発生頻度からある程度使われている文字が推測されてしまうこと。
