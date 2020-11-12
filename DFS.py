from Graph import Graph

WHITE = 0
GRAY = 1
BLACK = 2

# init

G = Graph()
colors = [WHITE] * G.size()
parents = [-1] * G.size()
first = [0] * G.size()
last = [0] * G.size()

has_cycle = False
start_cycle = None
end_cycle = None
time = 0


def dfs(G, u):
    """
    recursion implementation to DFS
    Complexity: O(|V| + |E|)
    note: Time, first, last used for steps count
    :param G: Object that represent a graph, contain an adjacent lists per vertex
    :param u: base: The graph's root, induction step: parent
    :return: we used global vars, no return
    """
    global time, has_cycle, start_cycle, end_cycle

    colors[u] = GRAY
    time += 1
    first[u] = time

    node = G.adj_list[u].head_val
    while node is not None:
        v = node.data_val
        # if we already visit that node == cycle
        if not has_cycle and colors[v] == GRAY and parents[u] != v:
            has_cycle = True
            start_cycle = u
            end_cycle = v
        # case of new node
        if colors[v] == WHITE:
            colors[v] = GRAY
            parents[v] = u
            dfs(G, v)
        node = node.next_val
    colors[u] = BLACK
    time += 1
    last[u] = time

dfs(G, 1)
print ('colors', colors)
print ('parents', parents)
print ('first', first)
print ('last', last)


