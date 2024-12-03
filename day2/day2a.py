from aocd import data, submit

reports = [list(map(int, line.split())) for line in data.strip().split("\n")]

def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

safe_count = sum(is_safe(report) for report in reports)
submit(safe_count)