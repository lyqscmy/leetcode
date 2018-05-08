class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xs = []
        nums = sorted(nums)
        for i, v in enumerate(nums):
            i +=1
            print("{}:{}".format(i,v))
            if i != v:
               xs.append(i)
        return xs
        
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
outputs = [5,6]

a = sol.findDisappearedNumbers(nums)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
