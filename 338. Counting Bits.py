#BruteForce
class Solution:
    def countBits(self, n: int) -> List[int]:
        def dectobinary(a):     #Function to calculate binary of a number
            binary=""
            while a>0:
                rem=a%2
                binary=str(rem)+binary
                a//=2
            return binary       #End of function dectoBinary
        res=[0]*(n+1)       #result array
        for i in range(1,n+1):  #looping through the result array
            d=dectobinary(i)
            res[i]=d.count('1') #counting number of 1 in that binary representative
        return res

        