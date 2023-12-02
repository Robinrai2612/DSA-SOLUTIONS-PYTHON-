class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = []
        for i in words:
            for j in i:
                if chars.count(j) < i.count(j):
                    break
            else:
                result.append(len(i)) 
        return sum(result)
        