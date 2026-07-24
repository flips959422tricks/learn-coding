class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            left_char = s[left]
            while not left_char.isalnum() and left < right:
                left = left + 1
                left_char = s[left]

            right_char = s[right]
            while not right_char.isalnum() and left < right:
                right = right - 1
                right_char = s[right]
            
            if left < right and left_char.lower() != right_char.lower():
                return False
            
            left = left + 1
            right = right - 1
        
        return True
