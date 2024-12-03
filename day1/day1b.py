from aocd import data, submit

lines = [tuple(map(int, line.split())) for line in data.strip().split("\n")]
left, right = zip(*lines)

res = sum(l * right.count(l) for l in sorted(left))

submit(res)