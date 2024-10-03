# Task Scheduler
def taskScheduler(tasks, n):
    frequencies = [0]*26
    for task in tasks:
        frequencies[ord(task) - ord('A')] += 1
    frequencies.sort()
    chunk = frequencies[-1] - 1
    idle_slots = chunk * n
    for i in range(24, -1, -1):
        idle_slots -= min(chunk, frequencies[i])
    return len(tasks) + max(0, idle_slots)

print(taskScheduler(["A", "A", "A", "B", "B", "B"], 2))
