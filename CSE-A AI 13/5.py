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
root=Node(2)
root.left=Node(3)
root.right=Node(1)
print("Bfs:")
bfs(root)