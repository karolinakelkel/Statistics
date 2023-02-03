class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length_of_string = len(s)

        #Case with a single symbol
        if length_of_string == 1:
            return False

        #  Case with a single repeated symbol
        if s.count(s[0]) == length_of_string:
            return True

        # Other cases
        substring = ''
        for symbol in s[:-1]:
            substring += symbol
            if len(substring) * s.count(substring) == length_of_string:
                return True

        return False
        return s in (s + s)[1:-1]




s = Solution()
print(s.repeatedSubstringPattern('habcabch'))




