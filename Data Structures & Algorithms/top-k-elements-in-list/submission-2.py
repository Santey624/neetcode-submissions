class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in hashmap.items():
            bucket[freq].append(num)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
            
            