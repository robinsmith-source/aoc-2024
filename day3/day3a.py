import re
from aocd import data, submit

res = 0

for a, b in re.findall(r"mul\((\d+),(\d+)\)", data):
    res += int(a) * int(b)

submit(res)
