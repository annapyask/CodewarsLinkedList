class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, res=None):
    if not head:
        return res
    next_n = head.next
    head.next = res
    return reverse(next_n, head)
