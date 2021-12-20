
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def colum_def(root, colum, map_):
    if root is None:
        return
    try:
        map_[colum].append(root.val)
    except:
        map_[colum] = [root.val]

    colum_def(root.left, colum - 1, map_)
    colum_def(root.right, colum + 1, map_)


def verticalOrder(root):
    map_ = dict()
    colum = 0
    colum_def(root, colum, map_)
    visited = []

    for i in range(len(map_)):
        visited.extend([map_[sorted(map_)[i]]])
    return visited


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(1)
root2.left.right = TreeNode(2)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(7)
root2.right.left.right = TreeNode(8)
root2.right.right.right = TreeNode(9)
root2.right.right.left = TreeNode(9)

root3 = TreeNode(9)
root3.left = TreeNode(2)
root3.right = TreeNode(5)
root3.left.left = TreeNode(3)
root3.left.right = TreeNode(4)
root3.left.right.left= TreeNode(1)
root3.right.right = TreeNode(6)
