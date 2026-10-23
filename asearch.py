
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

start = input("Enter start: ").upper()
goal = input("Enter goal: ").upper()

open_list = [(h[start], 0, start, [start])]
visited = set()

while open_list:
    open_list.sort()
    f, cost, node, path = open_list.pop(0)

    if node == goal:
        print("Path:", " -> ".join(path))
        print("Cost =", cost)
        break

    if node in visited:
        continue

    visited.add(node)

    for next_node, edge_cost in graph[node]:
        if next_node not in visited:
            new_cost = cost + edge_cost
            new_f = new_cost + h[next_node]
            open_list.append(
                (new_f, new_cost, next_node, path + [next_node])
            )
else:
    print("Path not found")
