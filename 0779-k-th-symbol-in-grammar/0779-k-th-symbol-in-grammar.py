class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def f(k):
            if k==1: return 0
            b=(int)(math.log2(k))
            if k==1<<b: return b%2
            else: return 1-f(k-(1<<b))
        return f(k)
        