class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0:
        raise IndexError
    lst = []
    cur = node
    while cur:
        lst.append(cur.data)
        cur = cur.next
    final = lst[index]
    return Node(final)
