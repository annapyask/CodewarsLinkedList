class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def swap_pairs(head):
    node_main = Node()
    node_main.next = head
    cur = node_main
    while cur.next and cur.next.next:
        current = cur.next
        next_node = current.next
        cur.next = next_node
        current.next = next_node.next
        next_node.next = current
        cur = current
    return node_main.next
