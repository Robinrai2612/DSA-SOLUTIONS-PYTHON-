class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        result = []
        i = 1 
        for t in target:
            while i < t:
                stack.append(i)
                result.extend(["Push", "Pop"])
                i += 1
            stack.append(t)
            result.append("Push")
            i += 1

        return result