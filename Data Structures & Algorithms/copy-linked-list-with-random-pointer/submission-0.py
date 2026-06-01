"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_mappings = {}
        def makeNewNodes(orig_node):
            if not orig_node:
                return None
            new_node = Node(orig_node.val, makeNewNodes(orig_node.next))
            node_mappings[(orig_node.val, orig_node.next)] = new_node
            return new_node
        
        new_head = makeNewNodes(head)
        current = head
        new_current = new_head
        while current and new_current:
            if current.random:
                new_random = node_mappings[(current.random.val, current.random.next)]
                new_current.random = new_random
            current = current.next
            new_current = new_current.next
        return new_head
        
        