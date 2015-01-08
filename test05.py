# -*- coding: utf-8 -*-

a = ('bob', 'john')

def greet(b):
	print 'hello {0}'.format(b)

for i in a:
	greet(i)
