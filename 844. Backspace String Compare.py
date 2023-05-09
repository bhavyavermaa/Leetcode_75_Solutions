class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def create(s1):
            stack=[]
            for i in s1:
                if i!="#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return create(s)==create(t)