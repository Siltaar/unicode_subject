#!/usr/bin/python3
# coding: utf-8
# author : Simon Descarpentries, 2017-03
# licence: GPLv3

import io, sys
from email.header import decode_header as d
from email.header import make_header as m

in_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
print(next(m(d(line)) for line in in_stream if line.startswith('ubject', 1)))
