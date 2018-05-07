sol = Solution()
S = "loveleetcode"
C = 'e'
outputs = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

a = sol.shortestToChar(S, C)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
