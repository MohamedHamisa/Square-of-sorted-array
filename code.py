class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums) # create a result list with dummy values
        i = len(nums) - 1 # index on which we will fill the result

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):.s.s.s.s.
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1 # we have filled the result on this index, now we go to the index one lesser than this
        return res



