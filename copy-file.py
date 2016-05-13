import sys
import os.path
import shutil

for f in os.listdir(sys.argv[1]):
shutil.copy(os.path.join(sys.argv[1], f), sys.argv[2])
