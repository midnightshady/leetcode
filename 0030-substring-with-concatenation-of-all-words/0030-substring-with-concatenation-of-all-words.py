class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        
        words_count = {}
        word_length = len(words[0])
        total_length = word_length * len(words)

        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        for i in range(word_length):
            left = i
            count = 0
            sub_count = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                sub_word = s[j : j + word_length]
                if sub_word in words_count:
                    sub_count[sub_word] = sub_count.get(sub_word, 0) + 1
                    count += 1
                    while sub_count[sub_word] > words_count[sub_word]:
                        sub_count[s[left:left + word_length]] -= 1
                        count -= 1
                        left +=  word_length
                    if count == len(words):
                        result.append(left)
                else:
                    sub_count.clear()
                    count = 0
                    left = j + word_length
        return result
                    