#!/usr/bin/env python3
import sys

# Read all input (as text)
data = sys.stdin.read()

# Split into lines (without keeping newline chars)
lines = data.splitlines()

# Dedupe + sort
out = sorted(set(lines))

# Write back (ensure trailing newline if there is output)
sys.stdout.write("\n".join(out))
if out:
    sys.stdout.write("\n")