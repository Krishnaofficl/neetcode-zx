class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #with hashmap(dict)
        if len(s1)>len(s2):
            return False
        k = len(s1)
        count1={}
        count2={}

        for i in range(k):
            count1[s1[i]]=1+count1.get(s1[i],0)
            count2[s2[i]]=1+count2.get(s2[i],0)

        if count1==count2:
            return True
        
        l=0
        for r in range(k,len(s2)):
            count2[s2[r]]=1+count2.get(s2[r],0)
            count2[s2[l]]-=1
            
            if count2[s2[l]]==0:
                del count2[s2[l]]
            l+=1
            
            if count2 == count1:
                return True

        return False