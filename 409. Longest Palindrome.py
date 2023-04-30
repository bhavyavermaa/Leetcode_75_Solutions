class Solution:
    def longestPalindrome(self, s: str) -> int:
        pair_counter=0
        unpaired_character=set()
        for i in s:
            if i in unpaired_character:
                pair_counter+=1
                unpaired_character.remove(i)
            else:
                unpaired_character.add(i)
        if unpaired_character:
            return pair_counter*2+1
        else:
            return pair_counter*2