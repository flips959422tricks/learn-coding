class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # easy exit, if k >= len(s) - 1, ans = s.length
        # brute force - simply start with every new char and start counting with tolerance
        # if you reach end of string, start moving the left pointer till you exhaust substitutions
        char_index = 0
        next_diff_char_index = 0
        max_length = 0
        
        while char_index < len(s):
            c = s[char_index]
            p = char_index # pointer
            reached_end = False
            max_for_char = 0
            subs_left = k

            while p >= 0 and p <= len(s)-1 and subs_left >= 0:
                # use a substitution
                if s[p] != c:
                    subs_left -= 1
                
                if subs_left < 0:
                    continue

                max_for_char += 1
                max_length = max(max_length, max_for_char)

                # flip traverse direction
                if p == len(s) - 1:
                    reached_end = True
                    p = char_index

                if not reached_end:
                    p += 1
                else:
                    p -= 1

            # increment and termination
            if next_diff_char_index > char_index:
                char_index = next_diff_char_index
            else:
                char_index += 1
        
        return max_length
        