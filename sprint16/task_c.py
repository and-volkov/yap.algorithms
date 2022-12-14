# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx):
    # Your code
    # ヽ(´▽`)/
    if idx == 0:
        next_node = get_node_by_index(node, idx + 1)
        node.next_item = None
        return next_node
    previous_node = get_node_by_index(node, idx - 1)
    target_node = get_node_by_index(node, idx)
    previous_node.next_item = target_node.next_item
    target_node.next_item = None
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head_2 = solution(node0, 2)
    assert new_head_2 is node0
    assert new_head_2.next_item is node1
    assert new_head_2.next_item.next_item is node3
    assert new_head_2.next_item.next_item.next_item is None
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head_3 = solution(node0, 0)
    assert new_head_3 is node1
    assert new_head_3.next_item is node2
    assert new_head_3.next_item.next_item is node3
    assert new_head_3.next_item.next_item.next_item is None
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head_3 = solution(node0, 3)
    assert new_head_3 is node0
    assert new_head_3.next_item is node1
    assert new_head_3.next_item.next_item is node2
    assert new_head_3.next_item.next_item.next_item is None


if __name__ == "__main__":
    test()
