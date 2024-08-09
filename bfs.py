from binarytree import Node
from collections import deque
def bfs(root):
    if not root:
        return
    queue=deque([root])
    while queue:
        node=queue.popleft()
        print(node.value,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print("Bfs traversal of tree is:")
bfs(root)
