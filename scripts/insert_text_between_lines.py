#!/usr/bin/env python3
import sys

first = True
for line in sys.stdin:
    if not first:
        sys.stdout.write("Python was here!\n")
    sys.stdout.write(line)
    first = False
