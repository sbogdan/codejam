#!/usr/bin/env python3
import random
import sys

numTests = int(sys.argv[1])
size = int(sys.argv[2])
fout = sys.stdout

fout.write(str(numTests) + "\n")

for _ in range(numTests):
    fout.write(str(size) + "\n")
    v = [str(random.randint(0, 20)) for _ in range(size)]
    fout.write(' '.join(v) + "\n")
