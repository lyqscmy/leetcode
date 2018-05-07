class Solution:
    VOWEL = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        new_words = []
        words = S.split(" ")
        for i, word in enumerate(words):
            new_word = "a" * (i + 1)
            if word[0] in Solution.VOWEL:
                new_word = "{}ma{}".format(word, new_word)
            else:
                new_word = "{}{}ma{}".format(word[1:], word[0], new_word)
            new_words.append(new_word)
        return " ".join(new_words)


sol = Solution()
S = "I speak Goat Latin"
outputs = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

a = sol.toGoatLatin(S)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

S = "The quick brown fox jumped over the lazy dog"
outputs = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
a = sol.toGoatLatin(S)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)

S = "Each word consists of lowercase and uppercase letters only"
outputs = "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"
a = sol.toGoatLatin(S)
b = outputs
try:
    assert a == b
except:
    print(a)
    print(b)
