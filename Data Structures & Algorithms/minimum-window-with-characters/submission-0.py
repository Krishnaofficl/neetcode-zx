class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        countT=Counter(t)
        window={}

        res,resL=[-1,-1],float("inf")
        have,need = 0,len(countT)
        
        l=0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1+window.get(ch,0)

            if ch in countT and window[ch] == countT[ch]:
                have+=1

            while have == need:
                #update result
                if r-l+1 < resL:
                    res = [l,r]
                    resL = r-l+1
                #pop from left
                window[s[l]] -=1 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        l,r = res
        return s[l:r+1] if resL != float('inf') else ""