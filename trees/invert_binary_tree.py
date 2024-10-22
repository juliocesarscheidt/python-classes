class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def invertTree(root):
    if root is None:
        return

    if root.left is not None or root.right is not None:
        [root.right, root.left] = [root.left, root.right]

    invertTree(root.left)
    invertTree(root.right)

    return root


def preorder(root):
  if root is None:
    return

  print(root.val, end=' ')
  preorder(root.left)
  preorder(root.right)


if __name__ == '__main__':
  '''
  Construct the following tree
            1
          /   \
        2       3
       / \     / \
      4   5   6   7
      
      Inverted tree
            1
          /   \
        3       2
       / \     / \
      7   6   5   4
  '''

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  
  preorder(root)
  # 1 2 4 5 3 6 7

  print('')

  invertTree(root)
  preorder(root)
  # 1 3 7 6 2 5 4
