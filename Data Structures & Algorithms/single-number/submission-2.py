class Solution:
    # THis solution is not accepted because the space complexity is O(n)
    #but the solution requires O(1) for space complexity. Time complexity is okay
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1

        for key, value in count.items():
            if value == 1:
                return key