from collections import deque
Max=15
n=0
if n>Max:
    exit()
graph={}
def input_graph():
    n=int(input("Enter the no of shelves:"))
    for i in range(n):
        node=int(input("Entr the node:"))
        graph[node]=[]
    for i in range(n):
        u=int(input("Enter the source node:"))
        v=input("enter the dest node:")
        list2=v.split()
        int_list = list(map(int,list2))
        graph[u]=int_list
def bfs(st,dest):
    visited=[]
    path=[]
    fringe=[]
    fringe.append(st)
    visited.append(st)
    index=0
    while fringe:
        print("\nfringe:",fringe)
        node=fringe.pop(0)
        path.append(node)
        print("\nvisited so far",path)
        if node==dest:
            print("\nGoal found")
            print("\nfinal path is",path)
            print("\nThe total cost is",len(path)*5)
            return
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                fringe.append(i)
        index=index+1
    print("\ngoal not  reached")
    return
def dfs(st,dest):
    visited=[]
    path=[]
    fringe=[]
    fringe.append(st)
    visited.append(st)
    index=0
    while fringe:
        print("\nfringe:",fringe)
        node=fringe.pop()
        path.append(node)
        print("\nvisited so far",path)
        if node==dest:
            print("\nGoal found")
            print("\nfinal path is",path)
            return
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                fringe.append(i)
        index=index+1
    print("\ngoal not  reached")
    return
while True:
    print("1)add node \n 2)add edge\n3)delete edge\n4)display\n5)delete node \n6)BFS\n7)DFS\n8)input graph")
    ch=int(input("Enter the choice:"))
    if ch==1:
        if len(graph)>Max:
            print("state space full")
        else:
            node=int(input("Enter the new node:"))
            graph[node]=[]
            print("node added")
            n=n+1
    elif ch == 2:
        u = int(input("Source node: "))
        v_list = list(map(int, input("Destination nodes (space separated): ").split()))
        if u not in graph: graph[u] = []
        for v in v_list:
            if v not in graph: graph[v] = []
            if v not in graph[u]: graph[u].append(v)
            if u not in graph[v]: graph[v].append(u)
    elif ch==4:
        print(graph)
    elif ch==5:
        node=int(input("Enter a node to delete:"))
        if node in graph:
            for i in graph[node]:
                graph[i].remove(node)
        del graph[node]
    elif ch==6:
        st=int(input("Enter the source:"))
        dest=int(input("Enter the dest charging node:"))
        if st in graph and dest in graph:
            bfs(st,dest)
    elif ch==7:
            st=int(input("Enter the source:"))
            dest=int(input("Enter the destination charging node:"))
            if st in graph and dest in graph:
                dfs(st,dest)
    elif ch==8:
        input_graph()
    else:
        break
