class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
    
        for i in range(len(num) - 2):
            substring = num[i:i+3]
            if len(set(substring)) == 1:
                if substring > max_good:
                    max_good = substring

        return max_good
        