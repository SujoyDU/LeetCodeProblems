class BT:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def create_tree(lst):
    nodes = [None] * len(lst)
    for indx, val in enumerate(lst):
        nodes[indx] = BT(val)
        if indx == 0 : continue
        elif indx % 2 == 0:
            nodes[indx //2 - 1].right = nodes[indx]
        else:
            nodes[indx // 2].left = nodes[indx]
    return nodes[0]


def print_tree(tree):
    prev_level = 0
    level_vals =[]
    queue = [(tree,prev_level)]
    while queue:
        nodes, level = queue.pop(0)
        if prev_level != level:
            print('Level: ', prev_level, level_vals)
            prev_level = level

        if nodes:
            level_vals.append(nodes.data)
            if nodes.left or nodes.right:
                queue.append((nodes.left, level +1))
                queue.append((nodes.right, level + 1))
            else: level_vals.append(None)


    if level_vals :
        print('Level: ', prev_level, level_vals)


def return_duplicates_in_same_level(root):
    '''
    Uses level order traversal to figure out duplicate values in the same level
    '''
    q = [(root, 0)]

    duplicates_list = set([])
    node_level_occurences = set([])
    while len(q) > 0:
        node, level = q.pop(0)

        if (node.data, level) not in node_level_occurences:
            node_level_occurences.add((node.data, level))
        else:
            duplicates_list.add((node.data, level))

        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return duplicates_list




# node = create_tree([1,2,3,4,5,6])
# print_tree(node)
#
# lst = [1,2,3]
# root = create_tree(lst)
# print_tree(root)
# print('Duplicates:', return_duplicates_in_same_level(root))


# lst = [10,12,3,12,14,11,11,14,16,16,14,11,11]

lst = [1,2,3,4,5,6,4]
# lst=[1]
root = create_tree(lst)
print_tree(root)
print('Duplicates:', return_duplicates_in_same_level(root))

lst = [1,2,3,4,5,5,4]
root = create_tree(lst)
print_tree(root)
print('Duplicates:', return_duplicates_in_same_level(root))

