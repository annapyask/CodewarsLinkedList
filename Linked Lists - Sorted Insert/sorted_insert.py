class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    lst = []
    k = 0
    current = head
    while current:
        lst.append(current.data)
        current = current.next
    lst.append(data)
    lst = sorted(lst, reverse=True)
    for i in lst:
        if k == 0:
            final = Node(i)
            k += 1
        else:
            final = Node(i, final)
    return final
