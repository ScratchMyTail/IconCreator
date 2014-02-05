#!/usr/bin/env python

import os, sys
import Image

sizes = [152, 120, 80, 76, 58, 40, 29]

for infile in sys.argv[1:]:
	for s in sizes:
		print s
		outfile = str(s) + ".png"

		if infile != outfile:
			try:
				size = s, s
				im = Image.open(infile)
				im.thumbnail(size, Image.ANTIALIAS)
				im.save(outfile, "PNG")
			except IOError:
				print "cannot create thumbnail for '%s'" % infile
