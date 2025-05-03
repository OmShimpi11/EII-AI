g = {
    1 : [2,3,4],
    2 : [1,3],
    3 : [1,2,4],
    4 : [1,3]
}

def my_dfs(g,s):
    visited[s] = 1
    print(s)

    for c in g[s]:
        if not visited[c]:
            my_dfs(g,c)

visited = [0] * 5
my_dfs(g,2) 


def my_bfs(g,s):
    queue = [s]
    visited = [s]
    while queue:
        current = queue.pop(0)
        print(current)

        for c in g[current]:
            if c not in visited:
                queue.append(c)
                visited.append(c)

my_bfs(g,1)

