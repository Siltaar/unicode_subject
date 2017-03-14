#!/usr/bin/python
# coding: utf-8
# author : Simon Descarpentries, 2017-03
# licence: GPLv3

# from __future__ import print_function, unicode_literals
from email.header import decode_header
import fileinput
import sys


for line in fileinput.input():
	if line.lower().startswith('subject:'):
		# print('debug '+line, file=sys.stderr)
		print(' '.join(
				[
					unicode(txt, enc if enc else 'utf8')
					for txt, enc in decode_header(line)
				]
			).encode('utf8')
		)
		break
