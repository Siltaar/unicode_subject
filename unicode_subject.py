#!/usr/bin/python3
# coding: utf-8
# author : Simon Descarpentries, 2017-03
# licence: GPLv3

import io, sys
from email.header import decode_header as d
from email.header import make_header as m

instream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
print(next(m(d(l)) for l in instream if l.startswith('ubject', 1)))
