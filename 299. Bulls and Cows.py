class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = 0
        sec = set()
        gus = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count += 1
            gus.add(guess[i])
            sec.add(secret[i])
        a = gus.intersection(sec)
        cow = 0
        for j in a:
            cow += min(secret.count(j),guess.count(j))
    
        c = str(count)+"A"+str(cow-count)+"B"
        return c
        
        