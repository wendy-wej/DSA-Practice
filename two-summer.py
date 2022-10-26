nums = [0,1,2,3,4,5,6,7,8,9,10,11]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        for i in nums:
            for j in range(x, len(nums)):
                if (i + nums[j] == target):
                    print([nums.index(i), j])
            x = x + 1
twoSum()