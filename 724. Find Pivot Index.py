class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forward=0
        backward=0
        for i in range(len(nums)):
            forward=sum(nums[:i])
            backward=sum(nums[i+1:])
            if forward==backward:
                return i
            else:
                continue
        return -1