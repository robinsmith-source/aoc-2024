import re
from aocd import data, submit

res = 0
enabled = True

for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
	if do or dont:
		enabled = bool(do)
	else:
		res += int(a) * int(b) * enabled

submit(res)