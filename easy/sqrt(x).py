import math

class Solution:
    def mySqrt(self, x: int) -> int:
        skibidi = math.sqrt(x)
        floor = math.floor(skibidi)
        return floor
    
if __name__=="__main__":
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))