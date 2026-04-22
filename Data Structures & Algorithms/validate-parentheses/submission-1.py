class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cts = {"}":"{","]":"[",")":"("}
        for ch in s:
            if ch in cts:
                if stack and stack[-1] == cts[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
            
        return True if not stack else False