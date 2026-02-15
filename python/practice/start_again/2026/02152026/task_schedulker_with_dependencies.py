# Task Scheduler Dependencies

from collections import defaultdict, deque
def task_scheduler(tasks, dependencies):
    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    for task, dep in dependencies:
        graph[dep].append(task)
        in_degree[task] += 1
    queue = deque([t for t in tasks if in_degree[t] == 0])
    order = []
    while deque:
        current = deque.popleft()
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                deque.append(neighbor)
    if len(order) != len(tasks):
        return [] 
    return order
