def loop_size(node):
    if node:
        k = 1
        current = node
        a = node.next
        b = node.next.next
        while a != b:
            k += 1
            current = current.next
            a = a.next
            b = b.next.next
        cur = b
        k = 1
        while current != cur:
            k += 1
            cur = cur.next
        return k
