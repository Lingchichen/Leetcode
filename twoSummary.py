class Solution:
    # brute force
    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                else:
                    pass
        return res

    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target - num], i])
            hash_table[num] = i
        return([])
