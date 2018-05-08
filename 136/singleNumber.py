class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums)
        # [low:mid].size % 2 != 0
        # singleNumber in [low:high]
        # high index the singleNumber
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 != 0:
                mid += 1
            if nums[mid] == nums[mid - 1]:
                high = mid - 2
            else:
                low = mid
        return nums[high]


sol = Solution()
nums = [2, 2, 1]
outputs = 1

a = sol.singleNumber(nums)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

nums = [4, 1, 2, 1, 2]
outputs = 4

a = sol.singleNumber(nums)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

nums = [
    17, 12, 5, -6, 12, 4, 17, -5, 2, -3, 2, 4, 5, 16, -3, -4, 15, 15, -4, -5,
    -6
]
outputs = 16

a = sol.singleNumber(nums)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
