class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    lst = []
    k = 0
    current = head
    while current:
        lst.append(current.data)
        current = current.next
    lst1 = lst[::2][::-1]
    lst2 = lst[1::2][::-1]
    for i in lst1:
        if k == 0:
            final1 = Node(i)
            k += 1
        else:
            final1 = Node(i, final1)
    k = 0
    for i in lst2:
        if k == 0:
            final2 = Node(i)
            k += 1
        else:
            final2 = Node(i, final2)
    return Context(final1, final2)
