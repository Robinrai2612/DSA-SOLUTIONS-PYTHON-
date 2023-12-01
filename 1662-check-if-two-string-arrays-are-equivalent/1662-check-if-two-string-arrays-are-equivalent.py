class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return sum(map(len,word1)) == sum(map(len,word1)) and ''.join(word1) == ''.join(word2)
        