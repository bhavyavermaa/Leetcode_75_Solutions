class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split(' ') #Converting the string into a list and storing
        st=st[::-1] #Reversing the list
        res=""  #Result string
        for i in st: #Looping throught the list
            if i!="": #Checking for extra spaces
                res=res+i+" " #Appending in the result string
        res=res.strip() # Removing Trailing space 
        return res