#!/usr/bin/env Python3
# -*- encoding:utf_8 -*-

import dictio

test = "Hello my name is Liodeus !"

for letter in test.upper():
    if letter in dictio.alpha:
        dictio.alpha[letter] += 1

dictio.alpha = sorted(dictio.alpha.items(), key=lambda x: x[1], reverse=True)

summ = 0
for t in dictio.alpha:
    summ += t[1]

li = []
for s in dictio.alpha:
    if s[1] != 0:
        purcentage = int((s[1] / summ) * 100)
        fo = "{} : {} %".format(s[0], purcentage)
        print(fo)
