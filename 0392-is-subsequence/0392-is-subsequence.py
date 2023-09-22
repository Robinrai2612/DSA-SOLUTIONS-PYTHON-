class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Initialize two pointers for s and t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move the pointer in s to the next character
            j += 1  # Always move the pointer in t

        # If we've reached the end of s, it means s is a subsequence of t
        return i == len(s)
        