class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        current_string = []
        if len(s) == 1:
            return 1
        
        for x in range(len(s)-1):
            current_string = []
            current_string.append(s[x])
            for i in range(x + 1, len(s)):
                if s[i] not in current_string:
                    current_string.append(s[i])
                    if longest_length <= len(current_string):
                        longest_length = len(current_string)
                elif s[i] in current_string:
                    if longest_length <= len(current_string):
                        longest_length = len(current_string)
                    break
                else:
                    break
        return longest_length