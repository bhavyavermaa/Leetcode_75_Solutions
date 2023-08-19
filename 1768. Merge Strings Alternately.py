#Two pointer Approach
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]      #Result array
        m=len(word1)
        n=len(word2)
        i,j=0,0     #Initialising two pointers to zero
        while i<m or j<n:   #If any one of the strings must exist the loop will go on
            if i<m: #Alternate strings
                res+=word1[i]
                i+=1
            if j<n:
                res+=word2[j]
                j+=1
        return "".join(res) #Returning the result in string form

#One Pointer Approach
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        m=len(word1)
        n=len(word2)
        i=0
        l=max(m,n)
        while i<l:
            if i<m:
                res+=word1[i]
            if i<n:
                res+=word2[i]
            i+=1
        return "".join(res)