
class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None

    def __repr__(self):
        return self.data_val


class SLinkedList:
    def __init__(self):
        self.head_val = None

    def __repr__(self):
        node = self.head_val
        ngbrs_str = ''
        while node is not None:
            ngbrs_str += ' --> ' + str(node.data_val)
            node = node.next_val
        return ngbrs_str

    def append(self, data_val=None):
        new_node = Node(data_val)

        if self.head_val is None:
            self.head_val = new_node
            return
        tmp = self.head_val
        while tmp.next_val is not None:
            tmp = tmp.next_val
        tmp.next_val = new_node


class Graph:
    def __init__(self):
        self.adj_list = [SLinkedList() for i in range(8)]

        self.adj_list[0].append(2)
        self.adj_list[0].append(3)

        self.adj_list[1].append(2)
        self.adj_list[1].append(7)

        self.adj_list[2].append(0)
        self.adj_list[2].append(1)
        self.adj_list[2].append(3)

        self.adj_list[3].append(0)
        self.adj_list[3].append(2)

        self.adj_list[4].append(5)
        self.adj_list[4].append(7)

        self.adj_list[5].append(4)
        self.adj_list[5].append(6)

        self.adj_list[6].append(5)
        self.adj_list[6].append(7)

        self.adj_list[7].append(4)
        self.adj_list[7].append(6)
        self.adj_list[7].append(1)

    def size(self):
        return len(self.adj_list)

    def __repr__(self):
        g_str = ''
        for i in range(len(self.adj_list)):
            g_str += str(i) + ":" + repr(self.adj_list[i]) + '\n'
        return g_str



