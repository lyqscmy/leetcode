class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums

        raw = [col for row in nums for col in row]
        xs = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(raw[i * c + j])
            xs.append(row)
        return xs


sol = Solution()
nums = [[1, 2], [3, 4]]
r = 1
c = 4
outputs = [[1, 2, 3, 4]]

a = sol.matrixReshape(nums, r, c)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

nums = [[1, 2], [3, 4]]
r = 2
c = 4
outputs = [[1, 2], [3, 4]]

a = sol.matrixReshape(nums, r, c)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
