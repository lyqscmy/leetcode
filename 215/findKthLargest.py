import heapq


class Solution(object):
    def findKthLargest1(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = nums
        p = 0
        r = len(nums) - 1

        k0 = r - k + 1
        q = partition(A, p, r)
        while q != k0:
            if k0 < q:
                r = q - 1
            else:
                p = q + 1
            q = partition(A, p, r)
        return A[q]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1


sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
y = 5

a = sol.findKthLargest1(nums, k)
b = y
try:
    assert a == b
except:
    print(a)
    print(b)

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
y = 4

a = sol.findKthLargest1(nums, k)
b = y
try:
    assert a == b
except:
    print(a)
    print(b)
