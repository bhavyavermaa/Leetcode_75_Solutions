class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for idx,c in enumerate(s):
            if c not in d:
                if t[idx] in d.values():
                    return False
                else:
                    d[c]=t[idx]
            else:
                if d[c]!=t[idx]:
                    return False
        return True