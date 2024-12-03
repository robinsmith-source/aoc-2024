from aocd import data, submit

reports = [list(map(int, line.split())) for line in data.strip().split("\n")]

def is_strictly_increasing_or_decreasing(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe(report):
    if is_strictly_increasing_or_decreasing(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_strictly_increasing_or_decreasing(modified_report):
            return True
    return False

safe_count = sum(is_safe(report) for report in reports)
print("Number of safe reports:", safe_count)
submit(safe_count)