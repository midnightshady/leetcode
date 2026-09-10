class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in map1:
                if map1[letter] != word:
                    return False
            else:
                map1[letter] = word

            if word in map2:
                if map2[word] != letter:
                    return False
            else:
                map2[word] = letter

        return True

