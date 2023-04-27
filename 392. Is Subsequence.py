class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subseq_ptr=0
        st_ptr=0
        while subseq_ptr<len(s) and st_ptr<len(t):
            if s[subseq_ptr]==t[st_ptr]:
                subseq_ptr+=1
            st_ptr+=1
        return subseq_ptr==len(s)