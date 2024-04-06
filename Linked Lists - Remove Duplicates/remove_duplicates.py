class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    lst = []
    k = 0
    current = head
    while current:
        lst.append(current.data)
        current = current.next
    lst = set(lst)
    lst = list(lst)
    lst = sorted(lst, reverse=True)
    if lst:
        for i in lst:
            if k == 0:
                final = Node(i)
                k += 1
            else:
                final = Node(i, final)
        return final