class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value={}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in value:
                return[value[needed],i]
            value[nums[i]] = i

        return []