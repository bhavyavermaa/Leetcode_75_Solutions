#BruteForce
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2=len(str1),len(str2)
        def valid(k):
            if len1%k or len2%k:
                return False
            n1,n2=len1//k,len2//k
            base=str1[:k]
            return str1==n1*base and str2==n2*base
        m=min(len1,len2)
        for i in range(m,0,-1):
            if valid(i):
                return str1[:i]
        return ""
