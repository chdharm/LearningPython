class Solution:
    def isBST(self, root):
        if root == None:
            return True
        if root.left and root.data < root.left.data:
            return False

        if root.right and root.data > root.right.data:
            return False

        if not self.isBST(root.left) or not self.isBST(root.right):
            return False
        return True


