class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value={}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in value:
                return[value[needed],i]
            value[nums[i]] = i #This actually stores the key-> value pair so we have to do this. For first element it stores: [0,3] where 0 is the index and 3 is the value

        return []
