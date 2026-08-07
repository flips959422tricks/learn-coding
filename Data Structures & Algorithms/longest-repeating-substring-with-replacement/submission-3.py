class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        window_end = 0
        char_counts = {}
        
        max_length = 0

        while window_end < len(s):
            # find new char
            new_char = s[window_end]

            # include in totals
            char_counts[new_char] = char_counts.get(new_char, 0) + 1

            # check substitution usage
            max_char_count = max(list(char_counts.values()))
            subs_used = window_end + 1 - window_start - max_char_count

            # evict if exceeds
            if subs_used > k:
                char_to_evict = s[window_start]
                while s[window_start] == char_to_evict:
                    char_counts[char_to_evict] = char_counts.get(char_to_evict, 0) - 1
                    window_start += 1

            # update max length
            max_length = max(max_length, window_end - window_start + 1)

            # increment window end
            window_end += 1

        return max_length
        