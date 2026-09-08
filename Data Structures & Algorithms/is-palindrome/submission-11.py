class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_concat = ''.join(s.split()).lower()
        s_filter = ''.join(filter(str.isalnum, s_concat))
        s_list = list(s_filter)

        if len(s_filter) <= 1:
            return True

        i = 0

        while i < len(s_list)//2:
            p_start = s_list[i]
            p_end = s_list[-i-1]

            if p_start != p_end:
                return False

            i += 1

        return True
        
        