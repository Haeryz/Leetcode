class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = len(s) - 1
        while count >= 0 and s[count] == ' ':
            count -= 1
        length = 0
        while count >= 0 and s[count] != ' ':
            length += 1
            count -= 1
        return length
            
if __name__=="__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))