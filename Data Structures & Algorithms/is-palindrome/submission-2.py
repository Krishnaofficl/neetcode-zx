class Solution:
    def isPalindrome(self, s: str) -> bool:
        #my intuitive solution without any reference
        s1=''
        for ch in s:
            if ch.isalnum():
                s1+=ch.lower()

        print(s1)
        s=s1
        l,r=0,len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True