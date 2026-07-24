class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = True

        lft = 0
        rgt = len(s) - 1

        while lft < rgt:
            lft_char = s[lft].lower()
            lft_char_valid = self.is_alphanumeric(lft_char)
            while not lft_char_valid:
                lft = lft + 1
                lft_char = s[lft].lower()
                lft_char_valid = self.is_alphanumeric(lft_char)

            rgt_char = s[rgt].lower()
            rgt_char_valid = self.is_alphanumeric(rgt_char)
            while not rgt_char_valid:
                rgt = rgt - 1
                rgt_char = s[rgt].lower()
                rgt_char_valid = self.is_alphanumeric(rgt_char)
            
            if lft < rgt and lft_char != rgt_char:
                return False
            
            lft = lft + 1
            rgt = rgt - 1
        
        return is_palindrome

    
    def is_alphanumeric(self, c: str) -> bool:
        pattern = r"^[a-zA-Z0-9]$"
        return bool(re.match(pattern, c))