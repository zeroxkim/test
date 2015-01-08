# -*- coding: utf-8 -*-

test = "this is test string"

i = 1
test2 = ""

while i <= len(test):
	test2 = test2 + test[len(test) - i]
	i = i + 1

print test2
