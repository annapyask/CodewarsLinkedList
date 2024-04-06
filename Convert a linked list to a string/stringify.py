def stringify(node):
    string = ''
    current = node
    while current:
        string += str(current.data)
        string += ' -> '
        current = current.next
    string += 'None'
    return string
