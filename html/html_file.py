"""docstring"""
import subprocess

FILE = "index.html"
subprocess.check_call(['html5validator', FILE])
print("us")
