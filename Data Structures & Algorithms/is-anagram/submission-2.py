class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1="".join(sorted(list(s)))
        str2="".join(sorted(list(t)))
        return str1==str2