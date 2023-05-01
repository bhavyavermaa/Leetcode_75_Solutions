# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root is None:
        return []
      q=[root]
      res=[]
      while q:
        nxt_q=[]
        level=[]
        for root in q:
          level.append(root.val)
          if root.left:
            nxt_q.append(root.left)
          if root.right:
            nxt_q.append(root.right)
        res.append(level)
        q=nxt_q
      return res