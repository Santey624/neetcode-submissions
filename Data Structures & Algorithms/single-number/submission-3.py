class Solution:
    # THis solution is not accepted because the space complexity is O(n)
    #but the solution requires O(1) for space complexity. Time complexity is okay
    def singleNumber(self, nums: List[int]) -> int:
        result= 0
        for i in nums:
            result = i^result
        return result