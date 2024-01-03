class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        initial = bank[0].count("1")
        result =0
        for i in range(1, len(bank)):
            current = bank[i].count("1")
            if current:
                result += (initial * current )
                initial = current
            
        return result
        
        