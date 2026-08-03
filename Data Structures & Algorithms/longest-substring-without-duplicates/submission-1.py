class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        substring_start_index = 0
        max_substring_length = 0
        i = 0

        while i < len(s):
            c = s[i]

            if c in char_set:
                char_set = set()
                substring_start_index = i

            char_set.add(c)
            max_substring_length = max(max_substring_length, i - substring_start_index + 1)

            i += 1

        return max_substring_length