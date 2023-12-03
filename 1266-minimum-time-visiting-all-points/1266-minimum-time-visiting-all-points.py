class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        n=len(points)
        for i in range(n-1):
            ans+=max(abs(points[i+1][0] - points[i][0]),abs(points[i+1][1] -points[i][1]))
        return ans    
        