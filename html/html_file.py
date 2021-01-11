"""docstring"""
from bs4 import BeautifulSoup
f = open("index.html", "r")
print(f.read())
k = bool(BeautifulSoup(f.read(), 'html.parser').find())

print(k)
