class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #with array
        if len(s1)>len(s2):
            return False
        k = len(s1)
        count1=[0]*26
        count2=[0]*26

        for i in range(k):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1

        if count1==count2:
            return True
        
        l=0
        for r in range(k,len(s2)):
            count2[ord(s2[r])-ord('a')]+=1
            count2[ord(s2[l])-ord('a')]-=1
            l+=1

            if count2==count1:
                return True

        return False