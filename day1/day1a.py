from aocd import data, submit

lines = [tuple(map(int, line.split())) for line in data.strip().split("\n")]
left, right = zip(*lines)

res = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

submit(res)