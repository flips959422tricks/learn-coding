class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        window_end = 0
        char_counts = { s[0]: 1 }

        max_length = 0

        while window_end < len(s):
            # check window validity
            char_count_values = list(char_counts.values())
            subs_used = sum(char_count_values) - max(char_count_values, default=0)

            if subs_used > k:
                # invalid case
                char_to_evict = s[window_start]

                # update window and counts together
                char_counts[char_to_evict] = char_counts[char_to_evict] - 1
                window_start += 1
            else:
                # update max length
                max_length = max(max_length, window_end + 1 - window_start)

                # update window and counts together
                window_end += 1
                if window_end < len(s):
                    new_char = s[window_end]
                    char_counts[new_char] = char_counts.get(new_char, 0) + 1

        return max_length
