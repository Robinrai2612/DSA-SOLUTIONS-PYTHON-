class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length to make it easier to find predecessors
        words.sort(key=len)
        # Initialize a dictionary to store the longest chain for each word
        dp = {}

        # Initialize the result variable to store the maximum chain length
        max_chain_length = 1

        # Iterate through the words
        for word in words:
            # Initialize the chain length for the current word to 1
            dp[word] = 1
            # Generate all possible predecessors of the current word by removing one character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                # If the predecessor is in the dictionary, update the chain length
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            # Update the maximum chain length
            max_chain_length = max(max_chain_length, dp[word])

        return max_chain_length
        