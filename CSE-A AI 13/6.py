from binarytree import Node
def dfs(root):
    if not root:
        return 
    stack=[root]
    while stack:
        node=stack.pop()
        print(node.value,end=" ")
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
root=Node(2)
root.left=Node(1)
root.right=Node(3)
root.left.left=Node(5)
root.left.right=Node(4)
root.right.left=Node(7)
root.right.right=Node(8)
print("Dfs:")
dfs(root)
