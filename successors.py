from collections import deque

def successors(n):
    a, b = n
    suc = []
    if a < 4: suc.append((4,b))
    if b < 3: suc.append((a,3))
    if a > 0: suc.append((0,b))
    if b > 0: suc.append((a,0))
    if (a < 4) and (b != 0):
        if b > 4 - a:
            suc.append((4, b - (4 - a)))
        else:
            suc.append((a + b, 0))
    if( a < 3 ) and (a != 0):
        if a > 3 - b:
            suc.append((a - ( 3 - b), 3))
        else:
            suc.append((0, b + a))

    return suc


parent = {}

def breadth_first_search(start):
    open = deque([start])
    closed = deque([])

    while open != []:
        n = open.popleft()
        if(n[0] == 2) or (n[1] == 2): return n

        closed.append(n)
        for m in successors(n):
            if m not in open and m not in closed:
                parent[m] = n
                open.append(m)

def main():
    start = (0,0)
    goal = breadth_first_search(start)

    n = goal
    print(n, end='')
    while n != start:
        n = parent[n]
        print("<-{0}".format(n), end='')


if __name__ == "__main__":
    main()