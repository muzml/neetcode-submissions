class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = "" 
        for i in s:
            if i.isalnum():
                m += i.lower()
        left = 0
        right = len(m)-1
        while left < right:
            if m[left] != m[right]:
                return False
            left += 1
            right -= 1
        return True
            
            
                