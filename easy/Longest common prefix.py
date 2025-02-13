from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Pseudocode:
        # 1. If strs is empty, return empty string.
        if (len(strs) == 0):
            return ""
        # 2. Determine the minimum length among all strings.
        min_length = min([len(s) for s in strs])
        # 3. For each index i from 0 to minimum length - 1:
        for i in range (min_length):
            #    a. Let current_char be the character at index i of the first string.
            current_char = strs[0][i]
            #    b. For each subsequent string in strs:
            for s in strs[1:]:
                #           - If the character at index i is not equal to current_char:
                if (s[i] != current_char):
                    #                * Return the prefix collected till now.
                    return s[:i]
        # 4. Return the prefix collected till now.
        return strs[0][:min_length]
            
if __name__=="__main__":
    s = Solution()
    print(s.longestCommonPrefix(strs=["flower","flow","flight"])) # Output: "fl"
    print(s.longestCommonPrefix(strs=["dog","racecar","car"])) # Output: "fl"