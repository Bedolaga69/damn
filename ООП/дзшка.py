import math
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node is None:
        return

    print(node.value)

    dfs_recursive(node.left)

    dfs_recursive(node.right)

def count_nodes_with_value(node, target_value):
    if node is None:
        return 0
    if node.value == target_value:
        count = 1
    else:
        count = 0
    return count + count_nodes_with_value(node.left, target_value) + count_nodes_with_value(node.right, target_value)

def find_max(node):
    if node is None:
        return -math.inf

    left_max = find_max(node.left)
    right_max = find_max(node.right)

    return max(node.value,left_max,right_max)


# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(52)
root.right.left = TreeNode(67)
root.right.right = TreeNode(42)

print("Depth-First Search (DFS) Recursive:")
dfs_recursive(root)

target_value = 5
count_of_target = count_nodes_with_value(root, target_value)
print(f"Количество узлов с числом {target_value}: {count_of_target}")


max_value = find_max(root)
print(f"Максимальный элемент в дереве: {max_value}")
