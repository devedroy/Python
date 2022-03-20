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
        adr2n = {None: None}
        
        cur = head
        while cur:
            adr2n[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            node = adr2n[cur]
            node.next = adr2n[cur.next]
            node.random = adr2n[cur.random]
            cur = cur.next
            
        return adr2n[head]
        