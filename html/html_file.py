"""docstring"""
from bs4 import BeautifulSoup
f = open("index.html", "r")
k = bool(BeautifulSoup(f.read(), 'lxml').find())

print(k)
