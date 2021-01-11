"""docstring"""
import tinycss
f = open("style.css", "r")

parser = tinycss.make_parser()
t = parser.parse_stylesheet(f.read()).errors

print(len(t))
