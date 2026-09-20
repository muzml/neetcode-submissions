class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = []
        for i in range(min(len(word1), len(word2))):
            l.append(word1[i])
            l.append(word2[i])
        l += word1[len(word2):]
        l += word2[len(word1):]
        return ''.join(l)