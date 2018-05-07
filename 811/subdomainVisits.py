class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        A = {}
        B = {}
        C = {}
        for cp in cpdomains:
            conut, address = cp.split(" ")
            conut = int(conut)
            domains = address.split(".")
            a = domains[-1]
            if not a in A:
                A[a] = conut
            else:
                A[a] += conut
            b = ".".join(domains[-2:])
            if not b in B:
                B[b] = conut
            else:
                B[b] += conut
            if len(domains) == 3:
                c = ".".join(domains)
                if not c in B:
                    C[c] = conut
                else:
                    C[c] += conut

        result = []
        for key, val in A.items():
            cp = "{} {}".format(val, key)
            result.append(cp)
        for key, val in B.items():
            cp = "{} {}".format(val, key)
            result.append(cp)
        for key, val in C.items():
            cp = "{} {}".format(val, key)
            result.append(cp)
        return result


sol = Solution()

xs = ["9001 discuss.leetcode.com"]
ys = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
a = set(sol.subdomainVisits(xs))
b = set(ys)
# print(a)
# print(b)
assert a == b

xs = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
ys = [
    "901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org",
    "5 org", "1 intel.mail.com", "951 com"
]

assert set(sol.subdomainVisits(xs)) == set(ys)
