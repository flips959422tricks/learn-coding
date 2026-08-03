class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index_map = {}
        substring_start_index = 0
        max_substring_length = 0
        i = 0

        while i < len(s):
            c = s[i]

            if c in char_to_index_map:
                substring_start_index = char_to_index_map[c] + 1
                del char_to_index_map[c]

            char_to_index_map[c] = i
            max_substring_length = max(max_substring_length, i - substring_start_index + 1)

            i += 1

        return max_substring_length
