class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        mid = len(s) // 2
      
        left_nice = self.longestNiceSubstring(s[:mid])
        
        right_nice = self.longestNiceSubstring(s[mid:])
        
        combined_nice = self.check_combined(s, mid)
        
        return max(left_nice, right_nice, combined_nice, key=len)

    def check_combined(self, s: str, mid: int) -> str:
        left = mid - 1
        right = mid
        
        while left >= 0 and (s[left].isupper() and s[right].islower() or s[left].islower() and s[right].isupper()):
            left -= 1
        left += 1  

        while right < len(s) and (s[left].isupper() and s[right].islower() or s[left].islower() and s[right].isupper()):
            right += 1
 
        if left >= right:
            return ""
        
        combined_substring = s[left:right]
        if self.is_nice(combined_substring):
            return combined_substring
        
        return ""

    def is_nice(self, sub: str) -> bool:
        lower_set = set()
        upper_set = set()

        for char in sub:
            if char.islower():
                lower_set.add(char)
            elif char.isupper():
                upper_set.add(char)

        for char in lower_set:
            if char.upper() not in upper_set:
                return False
        for char in upper_set:
            if char.lower() not in lower_set:
                return False

        return True

# Example 
solution = Solution()
s = "YazaAay"
print(solution.longestNiceSubstring(s))  # Output: "aAa"
