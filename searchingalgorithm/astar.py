import heapq

def astar(graph, start, goal, h):
    pq = []
    heapq.heappush(pq,(h[start], start))

    g = {start: 0}
    parent = {}

    print("\n--- A* Search Start ---\n")

    while pq:
        f, current = heapq.heappop(pq)
        print(f"f={f}  g={g[current]} h={h[current]}")
        print("path so far is :",backtrack(parent,current))

        if current == goal:
            print("\nGoal reached!\n")
            return backtrack(parent, goal)

        for neighbor, cost in graph[current]:
            new_g = g[current] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + h[neighbor]
                heapq.heappush(pq, (new_f, neighbor))
                print(f"Updated: g[{neighbor}]={new_g}, f={new_f}, parent={current}")

    return None


def backtrack(parent, node):
    path = [node]
    print("\n--- Backtracking Path ---")
    while node in parent:
        node = parent[node]
        path.append(node)
    path.reverse()
    return path
graph = {}
n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = [input() for _ in range(n)]
for node in nodes:
    graph[node] = []
e = int(input("Enter number of edges: "))
print("Enter edges in format: source destination cost")
for _ in range(e):
    u, v, c = input().split()
    c = int(c)
    graph[u].append((v, c))
print("\nEnter heuristic values:")
heuristic = {}
for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

path = astar(graph, start, goal, heuristic)

print("\nFinal Shortest Path:", path)
