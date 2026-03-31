class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            srtd_str=''.join(sorted(s))
            res[srtd_str].append(s)
        return list(res.values())