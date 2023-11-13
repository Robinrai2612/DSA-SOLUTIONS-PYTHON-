class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        consonants = []

        for char in s:
            if char in vowels:
                consonants.append(' ')  # Placeholder for vowels
            else:
                consonants.append(char)

        sorted_vowels = sorted([char for char in s if char in vowels])

        result = []
        vowel_index = 0

        for char in consonants:
            if char == ' ':
                result.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)

        return ''.join(result)
        