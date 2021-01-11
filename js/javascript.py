import subprocess
import os
import sys
filename = "java.js"
try:
    subprocess.check_call(['node', '--check', filename])
except subprocess.CalledProcessError:
    print(f"Found {filename} that that has syntactical errors.", file=sys.stderr)
