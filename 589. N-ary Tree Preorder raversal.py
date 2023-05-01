class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output=[]
        if root is None:
            return []
        stack=[root]
        while stack:
            top=stack.pop()
            output.append(top.val)
            stack.extend(reversed(top.children))
        return output