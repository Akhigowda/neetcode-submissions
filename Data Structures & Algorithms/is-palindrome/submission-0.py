class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        i = 0
        j = len(cleaned)-1
        while i<j:
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1

            else:
                return False
        
        return True


            
            
        
