class Solution:
    def helper(self, s):

        if not s: ""

        res = ""
        i = 0
        j = 0
        count = 0
        n = len(s)
        open_found = 0
        while i < n and j < n:
            
            if s[i].isdigit():

                j = i
                
                # Fetch count
                while j < n and s[j] != '[':
                    j += 1
                open_found = 1

                count = int(s[i:j])
                j += 1
                i = j

                # Fetch word
                while j < n and open_found != 0:
                    if s[j] == '[': open_found += 1
                    elif s[j] == ']':open_found -= 1
                    if open_found == 0: break
                    j += 1

                res += self.helper(s[i:j]) * count
                j += 1
                i = j

            else:
                res += s[i]
                i += 1
            
        return res

    def decodeString(self, s: str) -> str:
        return self.helper(s)