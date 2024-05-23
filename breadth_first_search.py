from collections import deque

graph = []
parent = [0] * 8

def gen_graph():
    graph.append([])
    graph.append([2,3,4])
    graph.append([5,6])
    graph.append([2,4,7])
    graph.append([7])
    graph.append([6])
    graph.append([3,7])

def breadth_first_search(start, goal):
    open = deque([start])
    closed = deque([])

    while open:  # open != [] の代わりに while open: を使用
        n = open.popleft()
        if n == goal:
            return

        closed.append(n)  # ループ内でノードを closed リストに追加

        for m in graph[n]:
            if m not in open and m not in closed:
                parent[m] = n
                open.append(m)

def main():
    gen_graph()
    start, goal = 1, 7
    breadth_first_search(start, goal)

    n = goal
    print(n, end='')
    while n != start:
        n = parent[n]
        print("<-{0}".format(n), end='')
    
if __name__ == "__main__":
    main()
