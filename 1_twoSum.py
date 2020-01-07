class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            print(i,num)
            if target - num in hash_table:
                return([hash_table[target - num], i])
            hash_table[num] = i
        return([])
