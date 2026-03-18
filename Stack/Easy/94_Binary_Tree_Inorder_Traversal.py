# Preorder Traversal of a Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        """
        Perform a recursive preorder traversal of a binary tree.
        :param root: TreeNode
        :return: List of node values in preorder (root -> left -> right)
        """
        if not root:
            return []

        # Combine current node with left and right subtree traversals
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )


# Example usage
if __name__ == "__main__":
    # Construct binary tree:
    #      2
    #     / \
    #    1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))

    solution = Solution()
    print(solution.preorderTraversal(root))  # Output: [2, 1, 3]
