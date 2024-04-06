class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s = s.strip().split(" -> ")
    s = s[::-1]
    s = s[1:]
    k = 0
    if s:
        for i in s:
            if k == 0:
                next = None
                current = Node(int(i), next)
                k += 1
            else:
                next = current
                current = Node(int(i), next)
        return current
