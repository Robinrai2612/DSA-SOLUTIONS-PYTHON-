class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_next_valid_char(s, index):
            backspace_count = 0
            while index >= 0:
                if s[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return index
                index -= 1
            return index

        s_ptr, t_ptr = len(s) - 1, len(t) - 1

        while s_ptr >= 0 or t_ptr >= 0:
            s_ptr = find_next_valid_char(s, s_ptr)
            t_ptr = find_next_valid_char(t, t_ptr)

            if s_ptr < 0 and t_ptr < 0:
                return True
            if s_ptr < 0 or t_ptr < 0 or s[s_ptr] != t[t_ptr]:
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True
        