import os.path
import sys

i = 100001
dirname = '/home'
for f in os.listdir(dirname):
	src = os.path.join(dirname,f)
	if os.path.isdir(src):
		continue
	os.rename(src,str(i))
	i += 1
