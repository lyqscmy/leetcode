class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        result = True
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        for j in range(n):
            e = matrix[0][j]
            i = 0
            while j < n and i < m:
                i += 1
                j += 1
                if matrix[i][j] != e:
                    result = False
                    break
            if not result:
                break

        for i in range(1, m):
            e = matrix[i][0]
            j = 0
            while j < n and i < m:
                i += 1
                j += 1
                if matrix[i][j] != e:
                    result = False
                    break
            if not result:
                break

        return result


sol = Solution()
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
outputs = True

a = sol.isToeplitzMatrix(matrix)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

matrix = [[1, 2], [2, 2]]
outputs = False

a = sol.isToeplitzMatrix(matrix)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

matrix = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
outputs = False

a = sol.isToeplitzMatrix(matrix)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
