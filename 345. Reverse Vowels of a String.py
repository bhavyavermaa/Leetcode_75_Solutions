#bruteForce
class Solution:
    def reverseVowels(self, s: str) -> str:
        v: set = { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" } # A set of vowels in all cases
            
        c: list[str] = list(s) # Creating a copy of the string passed
        l, r = 0, len(c) - 1 #Setting pointers left and right
        while l < r: #While left and right have not crossed each other.
            l_val, r_val= c[l], c[r] # Storing the value of pointer in local var
            if l_val in v and r_val in v: # Checking if both the value are vowels
                c[l], c[r] = c[r], c[l] #Swapping and then inc and dec pointer respectively
                l += 1 
                r -= 1 
            elif l_val in v and r_val not in v: # Left ptr is pointing to vowel but not right
                r-= 1
            elif l_val not in v and r_val in v: # Right ptr is pointing to vowel but not left
                l += 1
            else:   # Both pointers are not pointing to any vowel so change both value.
                l += 1
                r -= 1
        
        return "".join(c) #return string result.
