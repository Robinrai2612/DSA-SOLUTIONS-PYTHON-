class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0

        for char in s:
            if char.isalpha():
                decoded_length += 1
            elif char.isdigit():
                digit = int(char)
                decoded_length *= digit

        for char in reversed(s):
            k %= decoded_length
            if k == 0 and char.isalpha():
                return char
            if char.isalpha():
                decoded_length -= 1
            else:
                digit = int(char)
                decoded_length /= digit
