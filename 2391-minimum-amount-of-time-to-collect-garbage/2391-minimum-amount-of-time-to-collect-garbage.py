class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        peekGarbageTime = endM = endP = endG = 0
        i = len(garbage) - 1

        while i >=0:
            peekGarbageTime += len(garbage[i])
            if not endM and 'M' in garbage[i]: endM = i
            if not endP and 'P' in garbage[i]: endP = i
            if not endG and 'G' in garbage[i]: endG = i
            i -= 1

        dist = list(accumulate(travel, initial = 0))

        return dist[endM] + dist[endP] + dist[endG] + peekGarbageTime