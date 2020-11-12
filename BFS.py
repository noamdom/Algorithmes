from queue import Queue

from Graph import Graph

WHITE = 0
GRAY = 1
BLACK = 2


def bfs(G, root):
    """
    This function take the indexes as the vertex number
    Complexity O(|V| + |E|)
    :param G:
    :param root:
    :return:
    """
    # init
    colors = [WHITE] * G.size()
    distance = [-1] * G.size()
    parents = [-1] * G.size()
    q = Queue()

    colors[root] = GRAY
    distance[root] = 0
    parents[root] = 0
    q.put(root)

    while not q.empty():
        u = q.get()
        # look at u neighbour's <==> down tree level
        node = G.adj_list[u].head_val
        while node is not None:
            v = node.data_val
            if colors[v] == WHITE:
                colors[v] = GRAY
                distance[v] = distance[u] + 1
                parents[v] = u
                q.put(v)
            node = node.next_val
        colors[u] = BLACK

    print("colors: ", colors)
    print("distance: ", distance)
    print("parents: ", parents)


g = Graph()
bfs(g,1)