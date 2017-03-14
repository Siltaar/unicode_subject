#!/usr/bin/python2
# coding: utf-8
# author : Simon Descarpentries, 2017-03
# licence: GPLv3

import sys
from email.header import decode_header as d_h


for line in sys.stdin:
	if line.lower().startswith('subject:'):
		# sys.stderr.write('debug '+line)
		print ' '.join(
				[unicode(txt, enc or 'utf8') for txt, enc in d_h(line)]
			).encode('utf8')
		break
