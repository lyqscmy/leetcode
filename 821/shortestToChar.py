class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        low = 0  # index to lwo C
        xs = [0 for i in range(len(S))]

        for i in range(len(S)):
            if S[i] == C:
                low = i
                distance = 1
                for j in range(low - 1, -1, -1):
                    xs[j] = distance
                    distance += 1
                break

        for i in range(low + 1, len(S)):
            if S[i] == C:
                new_low = i
                mid = (low + new_low) // 2
                distance = 1
                for j in range(low + 1, mid + 1):
                    xs[j] = distance
                    distance += 1
                distance = 1
                for j in range(new_low - 1, mid, -1):
                    xs[j] = distance
                    distance += 1

                low = new_low

        distance = 1
        for i in range(low + 1, len(S)):
            xs[i] = distance
            distance += 1

        return xs


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

S = "aaba"
C = "b"
outputs = [2, 1, 0, 1]
a = sol.shortestToChar(S, C)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
