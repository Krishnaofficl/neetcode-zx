class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)>0:
            return "#;".join(strs)
        else:
            return 'None'
    def decode(self, s: str) -> List[str]:
        if s=='None':
            return []
        return s.split("#;")