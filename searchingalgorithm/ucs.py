import heapq
from platform import node
graph={}
def add_node(graph, nde):
    if node not in graph:
        graph[node] = []
        print(f"Node '{node}' added.")
    else:
        print("Node already exists.")

def delete_node(graph, node):
    if node in graph:
        graph.pop(node)
        for n in graph:
            graph[n] = [(v, c) for v, c in graph[n] if v != node]
        print(f"Node '{node}' deleted.")
    else:
        print("Node not found.")

def add_edge(graph, src, dest, cost):
    if src in graph and dest in graph:
        graph[src].append((dest, cost))
        print(f"Edge {src} -> {dest} with cost {cost} added.")
    else:
        print("Add nodes first.")

def delete_edge(graph, src, dest):
    if src in graph:
        graph[src] = [(v, c) for v, c in graph[src] if v != dest]
        print(f"Edge {src} -> {dest} deleted.")
    else:
        print("Source node not found.")

def display_graph(graph):
    print("\nCurrent Graph:")
    for node in graph:
        print(node, "->", graph[node])

def uniform_cost_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()
    print("\nUCS\n")
    while pq:
        cost, node, path = heapq.heappop(pq)
        #print(f"  Selected Node : {node}")
        #print(f"  Path So Far   : {path}")
        #print(f"  Cost So Far   : {cost}\n")
        print("\nFringe(priority queue -cost,node):",[(cost,node) for cost,node,_ in pq])
        print("path so far",path)
        print("current Node:",node,"with cost:",cost)
        if node == goal:
            print("GOAL NODE REACHED")
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_cost, neighbor, new_path))

    return None, float('inf')
def input_graph():
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input(f"Enter node {i+1}: ")
        graph[node] = []
    e = int(input("Enter number of edges: "))
    print("Enter edges in format: source destination cost")
    for _ in range(e):
        u, v, c = input().split()
        c = int(c)
        graph[u].append((v, c))

def main():

    while True:
        print("""
1. Add Node
2. Delete Node
3. Add Edge
4. Delete Edge
5. Display Graph
6. Uniform Cost Search (UCS)
7. Input
""")
        choice = int(input("Enter choice: "))

        if choice == 1:
            node = input("Enter node: ")
            add_node(graph, node)

        elif choice == 2:
            node = input("Enter node: ")
            delete_node(graph, node)

        elif choice == 3:
            src = input("Enter source node: ")
            dest = input("Enter destination node: ")
            cost = int(input("Enter cost: "))
            add_edge(graph, src, dest, cost)

        elif choice == 4:
            src = input("Enter source node: ")
            dest = input("Enter destination node: ")
            delete_edge(graph, src, dest)

        elif choice == 5:
            display_graph(graph)

        elif choice == 6:
            start = input("Enter start node: ")
            goal = input("Enter goal node: ")
            path, cost = uniform_cost_search(graph, start, goal)

            if path:
                print("\nFINAL RESULT")
                print("Shortest Path :", path)
                print("Total Cost    :", cost)
            else:
                print("No path found.")

        elif choice == 7:
            input_graph()

        else:
            print("Invalid choice.")
main()
