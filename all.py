# Task 1: Implement the in-order traversal algorithm for the given binary tree.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Task 2:  Implement the pre-order traversal algorithm for the given binary tree.
# In-order Traversal (Left, Root, Right):
def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)
# Pre-order Traversal (Root, Left, Right):
def preorder_traversal(node):
    if node is None:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

# Post-order Traversal (Left, Right, Root):
def postorder_traversal(node):
    if node is None:
        return []
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]

# Task 3: Implement the post-order traversal algorithm for the given binary tree.
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(40)
root.left.right = TreeNode(20)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# Task 4: Test the implemented traversal algorithms on a binary tree and observe the traversal order and output.
# In-order traversal 
print("In-order Traversal: ", inorder_traversal(root))

# Pre-order traversal
print("Pre-order Traversal: ", preorder_traversal(root))

# post-order traversal 
print("Post-order Traversal: ", postorder_traversal(root))

    


    