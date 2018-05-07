class Solution:
    AZ = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    MAX_UNITS = 100

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        width_map = {a: b for a, b in zip(Solution.AZ, widths)}
        line = 1
        width = 0

        for i in S:
            width += width_map[i]
            if width > Solution.MAX_UNITS:
                line += 1
                width = width_map[i]
        return [line, width]


sol = Solution()

widths = [
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10
]
S = "abcdefghijklmnopqrstuvwxyz"
outputs = [3, 60]
a = sol.numberOfLines(widths, S)
b = outputs
print(a)
print(b)
assert a == b

widths = [
    4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10
]
S = "bbbcccdddaaa"
outputs = [2, 4]

a = sol.numberOfLines(widths, S)
b = outputs
assert a == b
