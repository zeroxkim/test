# -*- coding: utf-8 -*-

a = 2

while a < 10:
	b = 1
	print '#{0} 단'.format(a)

	while b < 10:
		print '{0} X {1} = {2}'.format(a, b, a * b)
		b = b + 1

	print ''
	a = a + 1

