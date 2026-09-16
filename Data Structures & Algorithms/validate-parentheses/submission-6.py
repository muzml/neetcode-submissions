class Solution:
    def isValid(self, s: str) -> bool:
        seen = { ")":"(", "]":"[", "}":"{" }
        l = []
        for i in s:
            if i in seen:
                if not l or l[-1] != seen[i]:
                    return False
                l.pop()
            else:
                l.append(i)
        return not l