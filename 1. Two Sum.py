class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for idx,ele in enumerate(nums):
            d[ele]=idx
        for i in range(len(nums)):
            if target-nums[i] in d:
                if i!=d[target-nums[i]]:
                    return[i,d[target-nums[i]]]