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


def reverse_dictionary(dic):
    rev_dic = {}
    key = list(dic.keys())
    val = list(dic.values())
    for i in range(len(key)):
        rev_dic[val[i]] = key[i]
    return rev_dic
# 逆引き辞書の作成


if __name__ == '__main__':

    dic = make_dictionary()
    rev_dic = reverse_dictionary(dic)
    encode = []
    decode = []

    print("INPUT:")
    # 文字列の入力
    sentence = "In our previous work, we proposed a biometric authentication method using a secure imaging system that was based on compressed sensing. In this approach, although we can acquire an encrypted vein image, the verification process requires the restoration of the raw finger-vein image. To address this issue, we propose an improved authentication method that we can verify alternate biometric features from which it is difficult to restore the original finger-vein image by introducing the permutation matrix for randomizing the object signal. Numerical simulations show that our method has favorable accuracy, although it exhibits a slightly degraded accuracy in comparison with that of the conventional method that uses a raw finger-vein image. "
    print("plain:")
    print(sentence)

    # 暗号文の作成
    for char in range(len(sentence)):
        encode.append(dic[sentence[char]])

    # 復号文の作成
    for char in range(len(sentence)):
        decode.append(rev_dic[encode[char]])

    print("OUTPUT:")

    # 暗号文の出力
    print("encode:")
    for char in encode:
        print(char, end='')
    print("")

    # 復号文の出力
    print("decode:")
    for char in decode:
        print(char, end='')
    print("")
